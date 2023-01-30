from django.shortcuts import render, redirect
from shop.models import Product
from django.db.models import Q


# Create your views here.

def SearchResult(request):
    if request.GET.get('key')=='':
        return redirect('/')
    query = request.GET.get('key').upper()
    products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})

    # products = None
    # query=None
    # if 'q' in request.GET:
    #     query = request.GET.get('q')
    #     products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    # return render(request, 'search.html', {'query': query, 'products': products})
    # ^^^^^^^^^^the above hashed code generates error^^^^^^^^^^^^