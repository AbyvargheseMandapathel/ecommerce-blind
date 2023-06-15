from django.shortcuts import render, redirect
from .models import Product
from django.template import RequestContext


# Define a global variable to store the cart items
cart_items = []

def home(request):
    # Retrieve products from the database
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/home.html', context)

from django.shortcuts import render, redirect

def product_description(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        product = None

    context = {'product': product}
    return render(request, 'products/product_description.html', context)

def add_to_cart(request, product_id):
    # Retrieve the product from the database based on the product_id
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        product = None

    if product:
        quantity = int(request.POST.get('quantity', 1))

        # Create a dictionary representing the cart item
        cart_item = {'product': product, 'quantity': quantity}

        # Add the cart item to the global cart_items list
        cart_items.append(cart_item)

    return redirect('cart')

def cart(request):
    context = {'cart_items': cart_items}
    return render(request, 'products/cart.html', context)
