from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts, name='products'),
    path('<int:product_id>/', views.ProductDetail, name='product_detail'),
]