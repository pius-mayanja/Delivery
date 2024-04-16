from django.db import models
from user.models import User


class Business(models.Model):
    owner = models.OneToOneField(User, on_delete= models.CASCADE)
    business_name = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='business_images/')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contacts = models.CharField(max_length=200)
    
    
    class Meta():
        ordering = ['business_name']

    def __str__(self):
        return self.business_name

