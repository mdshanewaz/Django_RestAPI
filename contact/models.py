import email
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField( null = True, blank = True)

    def __str__(self): 
        return self.name