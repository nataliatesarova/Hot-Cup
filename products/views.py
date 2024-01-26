from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category,Product



def AllProducts(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None


    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You haven't entered any search terms. Please try again.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }
    
    return render(request, 'products/all_products.html', context)


def ProductDetail(request, product_id):
    """ View for displaying the details of a specific product based on its ID. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)