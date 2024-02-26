from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfileView, name='user_profile'),

]
