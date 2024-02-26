from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts, name='products'),
    path('<int:product_id>/', views.ProductDetail, name='product_detail'),
    path('add_review/', views.add_review, name='add_review'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('config/', views.stripe_config, name='stripe_config'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('wishlist/', views.get_wishlist, name='wishlist'),
    path('remove-from-wishlist/<int:item_id>/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]