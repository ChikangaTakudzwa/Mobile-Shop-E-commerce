from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from product.models import Product

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    # product id from the url
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')

# method to render the cart page
def cart(request):
    return render(request, 'cart/cart.html')


def update_cart(request, product_id, action):
    cart = Cart(request)

    # check to see if action is incrementing and then add 1 else remove 1
    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    # get products from the db
    product = Product.objects.all(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']

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

    response = render(request, 'cart/cart_item.html', item)
    response['HX-Trigger'] = 'update-menu-cart'

    return response

# method to render the checkout page
@login_required
def checkout(request):
    cart = Cart(request)
    context = {
        "cart": cart
    }
    return render(request, 'cart/checkout.html', context)

def hx_menu_cart(request):
    render(request, 'cart/menu_cart.html')