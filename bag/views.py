from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.db import transaction
from django.db.transaction import atomic
from django.views.decorators.http import require_POST
from django.views.generic import View
import logging

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe
import json

# Set up logging
logger = logging.getLogger(__name__)

def ViewShoppingBag(request):
    """ A view that renders the shopping bag contents page, including subtotal for each item. """
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    product_count = 0
    for item_id, quantity in bag.items():
        product = Product.objects.get(id=item_id)
        subtotal = product.price * quantity
        total += subtotal
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return render(request, 'bag/shopping_bag.html', context)


def checkout(request):
    return render(request, 'bag/checkout.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    print(item_id)
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Successfully Updated your bag')
    else:
        bag.pop(item_id)
        messages.success(request, f'Successfully Updated your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        logger.error(f'Error removing item {item_id}: {e}')
        return HttpResponse(status=500)


class CheckoutView(View):
    """
    View for handling the checkout process.

    Methods:
    - get: Renders the checkout page with an empty order form.
    - post: Handles the submission of the checkout form, creates an order,
            and processes the Stripe payment.
    """
    def get(self, request, *args, **kwargs):
        """
        Render the checkout page with an empty order form.

        Args:
        - request: The HTTP request object.

        Returns:
        - HTTP response rendering the checkout page.
        """
        order_form = OrderForm()
        return render(request, 'bag/checkout.html', {
            'order_form': order_form,
        })

    def post(self, request, *args, **kwargs):
        """
        Handle the submission of the checkout form.

        Args:
        - request: The HTTP request object.

        Returns:
        - HTTP response redirecting to the checkout success page if successful,
          otherwise redirecting to the shopping bag page.
        """
        bag = request.session.get('bag', {})  # Get the current bag from the session
        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'country': request.POST.get('country'),
            'postcode': request.POST.get('postcode'),
            'town_or_city': request.POST.get('town_or_city'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'county': request.POST.get('county'),
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            try:
                with atomic():  # Ensure all operations within this block are atomic
                    order = order_form.save(commit=False)  # Create order object but don't save to database yet
                    client_secret = request.POST.get('client_secret')
                    if client_secret:
                        pid = client_secret.split('_secret')[0]
                        order.stripe_pid = pid
                    else:
                        messages.error(request, 'Missing client secret. Please try again.')
                        return redirect(reverse('view_bag'))

                    order.original_bag = json.dumps(bag)
                    order.save()  # Save the order to the database

                    stripe.api_key = settings.STRIPE_SECRET_KEY
                    intent = stripe.PaymentIntent.create(
                        amount=int(order.grand_total * 100),  # Amount in cents
                        currency=settings.STRIPE_CURRENCY,
                        metadata={
                            'order_number': order.order_number,
                            'bag': json.dumps(bag),
                            'username': request.user.username if request.user.is_authenticated else 'AnonymousUser',
                        },
                    )

                    order.stripe_pid = intent.id
                    order.save()  # Save the updated order with stripe_pid

                    for item_id, item_data in bag.items():
                        try:
                            product = Product.objects.get(id=item_id)
                            if isinstance(item_data, int):
                                order_line_item = OrderLineItem(
                                    order=order,
                                    product=product,
                                    quantity=item_data,
                                )
                                order_line_item.save()  # Save each order line item
                        except Product.DoesNotExist:
                            messages.error(request, "One of the products in your bag wasn't found in our database. Please call us for assistance!")
                            logger.error(f"Product with id {item_id} not found. Deleting order {order.order_number}.")
                            order.delete()  # Delete the order if product not found
                            return redirect(reverse('view_bag'))

                    order.save()  # Ensure the order is saved after adding line items
                    request.session['save_info'] = 'save-info' in request.POST
                    return redirect(reverse('checkout_success', args=[order.order_number]))  # Redirect to success page with order number
            except Exception as e:
                logger.error(f"Error processing order: {e}")
                messages.error(request, 'There was an error processing your order. Please try again.')
                return redirect(reverse('view_bag'))
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
            logger.error('Order form invalid: {}'.format(order_form.errors))
        return redirect(reverse('view_bag'))


class CheckoutSuccessView(View):
    """
    View for handling successful checkouts.

    Methods:
    - get: Renders the checkout success page with the order details.
    """
    def get(self, request, order_number):
        """
        Render the checkout success page.

        Args:
        - request: The HTTP request object.
        - order_number: The order number of the successful order.

        Returns:
        - HTTP response rendering the checkout success page.
        """
        save_info = request.session.get('save_info')
        try:
            order = get_object_or_404(Order, order_number=order_number)  # Retrieve the order by order number
            messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

            if 'bag' in request.session:
                del request.session['bag']  # Clear the bag from the session

            template = 'bag/checkout_success.html'
            context = {
                'order': order,
            }

            return render(request, template, context)  # Render the success page with the order context
        except Exception as e:
            logger.error(f"Error retrieving order {order_number}: {e}")
            messages.error(request, 'There was an error processing your request. Please try again.')
            return redirect(reverse('view_bag'))
