from django.urls import path
from . import views  # Replace with the actual view function you'll use

urlpatterns = [
    path('', views.UserProfileView, name='user_profile'),

]
