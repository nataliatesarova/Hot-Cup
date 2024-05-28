from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create.

    Args:
        sender (Model): The model class.
        instance (Model instance): The actual instance being saved.
        created (bool): Whether this instance is being created.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete.

    Args:
        sender (Model): The model class.
        instance (Model instance): The actual instance being deleted.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()
