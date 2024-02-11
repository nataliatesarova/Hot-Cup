from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category,Product,Review,Wishlist
from django.contrib.auth.models import User



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

    try:
        reviews = Review.objects.filter(product_id=product_id)
        print(reviews)
    except Review.DoesNotExist:
        raise Http404("Given query not found....")

    context = {
        'product': product,
        'reviews': reviews,
    }
    
    return render(request, 'products/product_detail.html', context)

def add_review(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        text = request.POST.get('text')

        user = get_object_or_404(User, username=request.user.username)
        Review.objects.create(user=user, product_id=product_id, text=text)

    return redirect('product_detail', product_id=product_id)


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get or create the user's wishlist
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)

        # Add the product to the wishlist
        wishlist.products.add(product)

    # Redirect to the product detail page
    return redirect('product_detail', product_id=product_id)