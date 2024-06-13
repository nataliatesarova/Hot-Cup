from decimal import Decimal
import logging
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


logger = logging.getLogger(__name__)


def bag_contents(request):
    '''
    Handles the shopping bag contents
    '''
    logger.debug('Executing bag_contents context processor')

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    logger.debug(f'Current bag session: {bag}')

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
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    logger.debug(f'Context returned by bag_contents: {context}')
    return context
