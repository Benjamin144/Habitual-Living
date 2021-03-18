<<<<<<< HEAD
from django.shortcuts import render
from .models import Product

def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
=======
>>>>>>> 117bca8c17c3680e9f51d16c4217de1c277143bc
