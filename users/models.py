from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class Timestamps(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Users(AbstractUser, Timestamps):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    
