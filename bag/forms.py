from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for placing an order.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'country',
                  'postcode', 'town_or_city', 'street_address1',
                  'street_address2', 'county',)
