from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from product.models import Product
from django.conf import settings

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    # product id from the url
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')

# method to render the cart page
def cart(request):
    return render(request, 'cart/cart.html')


def update_cart(request, id, action):
    cart = Cart(request)

    # check to see if action is incrementing and then add 1 else remove 1
    if action == 'increment':
        cart.add(id, 1, True)
    else:
        cart.add(id, -1, True)

    # get products from the db
    product = Product.objects.get(pk=id)
    quantity = cart.get_item(id)

    if quantity:
        quantity = quantity['quantity']

        # dictionary to return to the cart
        item = {
            'product':{
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price
            },
            'total_price': (quantity * product.price),
            # 'total_price': (quantity * product.price) / 100 for dollar prices
            'quantity': quantity
        }
    else:
        item = None

    response = render(request, 'cart/cart_item.html', {'item': item})
    response['hx-trigger'] = 'update-menu-cart'

    return response

# method to render the checkout page
@login_required
def checkout(request):
    cart = Cart(request)
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
    context = {
        "cart": cart,
        "pub_key": pub_key
    }
    return render(request, 'cart/checkout.html', context)

# htmx method called when event is triggered, must have a return statement to work
def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

# htmx method called when event is triggered, must have a return statement to work
def hx_cart_total(request):
    return render (request, 'cart/cart_total.html')