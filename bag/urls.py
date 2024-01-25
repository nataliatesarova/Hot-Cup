from django.urls import path
from . import views


urlpatterns = [
    path('', views.ViewShoppingBag, name='view_bag'),
]