from django.conf import settings
from product.models import Product

class Cart(object):
    def __init__(self, request):
        # get session
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        # check to see if cart is created
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # methon to iterate through self.cart.keys()
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

    # methon to get length of cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    # methon for adding items to the cart
    def add(self, id, quantity=1, update_quantity=False):
        # convert id into string for easy access
        id = str(id)

        # check if product id is in the cart if not add it
        if id not in self.cart:
            # set default quantity to 1 and id to id
            self.cart[id] = {'quantity': 1, 'id': id} 
            # self.cart.setdefault(id, {'quantity': 0})['quantity'] = {'quantity': 1, 'id': id}

        if update_quantity:
            self.cart[id]['quantity'] += int(quantity)
            # check if the quantity is 0, and rm it from the cart
            if self.cart[id]['quantity'] == 0:
                self.remove(id)
            # self.save to save the updates and update the session
            self.save()

    # method to remove items from the cart
    def remove(self, id):
        # check to see if id is in cart and delete it
        if id in self.cart:
            del self.cart[id]
            self.save()