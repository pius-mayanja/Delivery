from django.db import models
from user.models import User
from business.models import Business


class Categories(models.Model):        #these are categories for all products in database
    category_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['category_name',]
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name

class Type(models.Model):
    category = models.ForeignKey(Categories, related_name='type',on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length = 250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits = 30, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    product_by = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    