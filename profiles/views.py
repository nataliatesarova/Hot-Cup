from django.shortcuts import render
from .models import UserProfile
from django_countries import countries

def UserProfileView(request):
    user_profile = UserProfile.objects.get(user=request.user)
    c = list(countries)
    context = {'user_profile': user_profile, "countries": c}
    return render(request, 'profiles/user_profile.html', context)
