
from django.shortcuts import render
from .models import Product, Currency

def product_list(request):
    products = Product.objects.all()
    
    currency = Currency.objects.first()

    converted_products = [
        {'name': product.name, 'price': product.price, 'converted_price': product.price * currency.rate}
        for product in products
    ]

    return render(request, 'index.html', {'products': converted_products})

