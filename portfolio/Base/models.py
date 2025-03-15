from django.db import models
from django.contrib import messages
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    content = models.TextField(max_length=400)
    number = models.CharField(max_length=13)
    
