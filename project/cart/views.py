from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
@login_required
def checkout(request):
    cart = Cart(request)
    context = {
        "cart": cart
    }
    return render(request, 'cart/checkout.html', context)