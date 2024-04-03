from django.db import models
from django.contrib.auth.models import User
from business.models import Business


class Categories(models.Model):
    category_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    class Meta:
        ordering = ['category_name',]
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    categories = models.ForeignKey(Categories, related_name='name',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null= True)
    
    def __str__(self):
        return self.name
        
class Type(models.Model):
    business = models.ForeignKey(Business, related_name='business', on_delete=models.CASCADE, null=True, blank=True)
    Product = models.ForeignKey(Product, related_name='items',on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length = 250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits = 30, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    product_by = models.ForeignKey(User, related_name = 'items', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    