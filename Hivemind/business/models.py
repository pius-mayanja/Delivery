from django.db import models
from django.contrib.auth.models import User


class Business(models.Model):
    owner = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='business_images/')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    contacts = models.CharField(max_length=200)
    
    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name
    
