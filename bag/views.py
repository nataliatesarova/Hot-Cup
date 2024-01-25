from django.shortcuts import render


def ViewShoppingBag(request):
    """ A view that renders the shopping bag contents page """

    return render(request, 'bag/shopping_bag.html')
