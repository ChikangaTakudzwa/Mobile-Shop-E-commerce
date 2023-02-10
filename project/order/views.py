from django.shortcuts import render, redirect
# from django.urls import redirect
from .models import Order, OrderItem
from cart.cart import Cart
import json
import stripe
from django.conf import settings
from django.http import JsonResponse

# When this function is called we talk to stripe and get the payment information from there.
def start_order(request):

    cart = Cart(request)

    data = json.loads(request.body)
    total_price = 0
    # list to send to stripe
    items = []

    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity'])
        # data expected by stripe > obj
        obj = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name
                },
                'unit_amount': product.price
            },
            'quantity': item['quantity']
        }
        items.append(obj)

    # get api key from settings file
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    # create stripe session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='https://*.gitpod.io/cart/success/',
        cancel_url='https://*.gitpod.io/cart/'
    )
    payment_intent = session.payment_intent

    # get form data from the data variable that uses json.loads
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']
    phone = data['phone']

    # createw order from form data
    order = Order.objects.create(
            user = request.user,
            first_name = first_name,
            last_name = last_name,
            email = request.user.email,
            address = address,
            zipcode = zipcode,
            place = place,
            phone = phone,
        )
    order.payment_intent = payment_intent
    order.paid_amount = total_price
    order.paid = True
    order.save()

    # loop through items in the cart and get the product, quantity and total price
    for item in cart:
        product = item['product']
        quantity = item['quantity']
        price = product.price * quantity
        item = OrderItem.objects.create(
            order = order,
            product = product,
            price = price,
            quantity = quantity,
        )
    return JsonResponse({'session': session, 'order': payment_intent})
