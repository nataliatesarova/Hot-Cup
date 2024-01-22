from django.shortcuts import render
from .models import Category,Product



def AllProducts(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/all_products.html', context)

