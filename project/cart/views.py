from django.shortcuts import render
from cart.cart import Cart

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    # product id from the url
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')

# method to render the cart page
def cart(request):
    return render(request, 'cart/cart.html')


# method to render the checkout page
def checkout(request):
    return render(request, 'cart/checkout.html')