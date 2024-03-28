from django.conf import settings
from jumia.models import Product, Type

 
class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Type.objects.get(pk=p)

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True 

    def add(self, type_id, quantity=1, update_quantity=False):
        type_id = str(type_id)

        if type_id not in self.cart:
            self.cart[type_id] = {'quantity':1, 'id':type_id}

        if update_quantity:
            self.cart[type_id]['quantity'] += int(quantity)

            if self.cart[type_id]['quantity'] == 0:
                self.remove(type_id)
        self.save()
    
    def remove(self, type_id):
        if type_id in self.cart:
            del self.cart[type_id]
            self.save()