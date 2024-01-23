from django.shortcuts import render, get_object_or_404
from .models import Category,Product



def AllProducts(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/all_products.html', context)


def ProductDetail(request, product_id):
    """ View for displaying the details of a specific product based on its ID. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)