from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts, name='products'),
]