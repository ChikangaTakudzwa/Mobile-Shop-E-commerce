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
            # strigfy id to access it as string and assign product proprty into p
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        # loop through the cart values
        for item in self.cart.values():
            item['total_price'] = item['product'].price * item['quantity']

            yield item

    # methon to get length of cart
    def __len__(self):

        # for each item in the cart we check what the quantity is and sum it to create one variable
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
            self.cart[id] = {'quantity': quantity, 'id': id} 
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

    def get_total(self):
        for p in self.cart.keys():
            # strigfy id to access it as string and assign product proprty into p
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return sum(item['product'].price * item['quantity'] for item in self.cart.values())

    def get_item(self, id):
        return self.cart[str(id)]

    # def get_total_cart_price(self):
    #     total = 0
    #     for item in self.cart.values():
    #         total += item['product'].price
    #     return total