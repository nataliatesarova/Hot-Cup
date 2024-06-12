from django.urls import path
from . import views
from .views import CheckoutView, CheckoutSuccessView
from .webhooks import webhook


urlpatterns = [
    path('', views.ViewShoppingBag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('checkout_success/<order_number>/', CheckoutSuccessView.as_view(), name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
