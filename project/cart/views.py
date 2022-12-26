from django.shortcuts import render
from cart.cart import Cart

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    # product id from the url
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')