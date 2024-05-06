from django.db import models
from user.models import User
from django.utils import timezone

class Business(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    
    class Meta():
        ordering = ['name']

    def __str__(self):
        """Returns a string representation of the business."""
        return self.name if self.name else 'not registered'
