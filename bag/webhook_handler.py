import json
import time
import logging
import stripe

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem

logger = logging.getLogger(__name__)


class StripeWHHandler:
    """
    Handle Stripe webhooks.
    """

    def __init__(self, request):
        """
        Initialize the handler with the request.
        """
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email.

        Args:
            order (Order): The order to send a confirmation for.
        """
        cust_email = order.email
        subject = render_to_string(
            'bag/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'bag/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.

        Args:
            event (dict): The event data from Stripe.
        Returns:
            HttpResponse: A response indicating the event was received.
        """
        logger.info(f'Unhandled webhook received: {event["type"]}')
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.

        Args:
            event (dict): The event data from Stripe.
        Returns:
            HttpResponse: A response indicating the event was received.
        """
        logger.info('Payment intent succeeded handler started')
        try:
            intent = event.data.object
            pid = intent.id
            bag = intent.metadata.bag
            save_info = intent.metadata.save_info

            billing_details = intent.charges.data[0].billing_details
            shipping_details = intent.shipping
            grand_total = round(intent.charges.data[0].amount / 100, 2)

            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None

            profile = None
            username = intent.metadata.username
            if username != 'AnonymousUser':
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.default_town_or_city = shipping_details.address.city
                    profile.default_street_address1 = shipping_details.address.line1
                    profile.default_street_address2 = shipping_details.address.line2
                    profile.default_county = shipping_details.address.state
                    profile.save()

            order_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    order = Order.objects.get(
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_or_city__iexact=shipping_details.address.city,
                        street_address1__iexact=shipping_details.address.line1,
                        street_address2__iexact=shipping_details.address.line2,
                        county__iexact=shipping_details.address.state,
                        grand_total=grand_total,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                    order_exists = True
                    break
                except Order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
            if order_exists:
                logger.info(f'Order {order.order_number} already exists in the database.')
                self._send_confirmation_email(order)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)
            else:
                order = None
                try:
                    logger.info('Creating a new order.')
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_bag=bag,
                        stripe_pid=pid,
                        grand_total=grand_total,
                    )
                    for item_id, item_data in json.loads(bag).items():
                        product = Product.objects.get(id=item_id)
                        if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                            order_line_item.save()
                    logger.info(f'Order {order.order_number} created successfully.')
                except Exception as e:
                    logger.error(f'Error creating order: {e}')
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)
            self._send_confirmation_email(order)
            logger.info(f'Confirmation email sent for order {order.order_number}.')
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)
        except Exception as e:
            logger.error(f'Error in handle_payment_intent_succeeded: {e}')
            return HttpResponse(content=f'Webhook error: {e}', status=500)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.

        Args:
            event (dict): The event data from Stripe.
        Returns:
            HttpResponse: A response indicating the event was received.
        """
        logger.info(f'Payment intent failed: {event["type"]}')
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
