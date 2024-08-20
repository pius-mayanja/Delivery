from django.db import models
from user.models import User
from django.utils import timezone

class Business(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """Returns a string representation of the business."""
        return self.username if self.username else 'not registered'
