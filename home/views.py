from django.shortcuts import render

from home.models import FAQ


def home(request):
    """ A view to render the home page """
    return render(request, 'home/index.html')

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'home/faq.html', {'faqs': faqs})
