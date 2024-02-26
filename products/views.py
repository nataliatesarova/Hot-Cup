from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product, Review, Wishlist
from django.contrib.auth.models import User
import stripe
from django.conf import settings
from django.http import Http404, JsonResponse
from decimal import Decimal


def AllProducts(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You haven't entered any search terms. Please try again.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/all_products.html', context)


def ProductDetail(request, product_id):
    """ View for displaying the details of a specific product based on its ID. """

    product = get_object_or_404(Product, pk=product_id)

    try:
        reviews = Review.objects.filter(product_id=product_id)
    except Review.DoesNotExist:
        raise Http404("Given query not found....")

    try:
        wishlist = Wishlist.objects.get(products=product, user=request.user)
    except:
        wishlist = None

    context = {
        'product': product,
        'reviews': reviews,
        'wishlist': wishlist
    }

    return render(request, 'products/product_detail.html', context)


def add_review(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        text = request.POST.get('text')

        user = get_object_or_404(User, username=request.user.username)
        Review.objects.create(user=user, product_id=product_id, text=text)

    return redirect('product_detail', product_id=product_id)


def get_wishlist(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user).products.all()

    except Wishlist.DoesNotExist:
        return render(request, 'products/wishlist.html', {})

    context = {
        'wishlist': wishlist
    }

    return render(request, 'products/wishlist.html', context)


def remove_from_wishlist(request, item_id, product_id):
    try:
        wishlist_item = Wishlist.objects.get(id=item_id)
        products = wishlist_item.products.all()
        for wl in products:
            if wl.id == product_id:
                wishlist_item.products.remove(wl)
        if len(Wishlist.objects.get(id=item_id).products.all()) == 0:
            wishlist_item.delete()
    except Wishlist.DoesNotExist:
        return HttpResponse(f"{item_id} not found in wishlist.")

    return redirect('product_detail', product_id=product_id)


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get or create the user's wishlist
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)

        # Add the product to the wishlist
        wishlist.products.add(product)

    # Redirect to the product detail page
    return redirect('product_detail', product_id=product_id)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        bag_items = []
        total = 0
        product_count = 0
        bag = request.session.get('bag', {})

        for item_id, quantity in bag.items():
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            delivery = 0

        grand_total = int((delivery + total) * 100)

        try:

            intent = stripe.PaymentIntent.create(
                amount=grand_total,
                currency='eur',
                automatic_payment_methods={
                    'enabled': True,
                },
            )

            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
