from django.shortcuts import render

from home.models import FAQ


def home(request):
    """ A view to render the home page """
    return render(request, 'home/index.html')


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'home/faq.html', {'faqs': faqs})


def successful(request):
    query_params = request.GET
    context = {
        'pi': query_params['payment_intent'],
        'rs': query_params['redirect_status']
    }
    return render(request, 'home/successful_checkout.html', context)