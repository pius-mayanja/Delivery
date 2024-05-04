from django.db import models 
from jumia.models import Type
from user.models import User
from decimal import Decimal, ROUND_HALF_UP
from business.models import Business



class Order(models.Model):  
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)    
    last_name = models.CharField(max_length=50)    
    email = models.EmailField()    
    address = models.CharField(max_length=250)    
    phone_number = models.CharField(max_length=20)    
    city = models.CharField(max_length=100)    
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)    
    paid = models.BooleanField(default=False)

    class Meta:        
        ordering = ['-created']        
        indexes = [           
             models.Index(fields=['-created']),        
             ]

    def __str__(self):        
        return f'Order {self.id}'
    
    def get_total_cost(self):        
        return sum(item.get_cost() for item in self.orders.all())
    
    def delivery(self):        
        total = self.get_total_cost()
        delivery_cost = total * Decimal('0.008')
        return delivery_cost.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
    
    def cost(self):        
        return self.delivery() + self.get_total_cost()
    
        
class OrderItem(models.Model):    
    order = models.ForeignKey(Order,related_name='orders',on_delete=models.CASCADE)    
    product = models.ForeignKey(Type,related_name='items',on_delete=models.CASCADE)    
    price = models.DecimalField(max_digits=10,decimal_places=2)    
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):        
        return self.price * self.quantity
    
    
