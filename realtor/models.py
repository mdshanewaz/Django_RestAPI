from datetime import datetime
from distutils.command.upload import upload
import email
from email.mime import image
from pyexpat import model
from tokenize import blank_re
from django.db import models
from datetime import datetime
from PIL import Image

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length = 100)
    biodata = models.TextField(null = True, blank = True)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 20)
    image = models.ImageField(upload_to = 'realtor', null = True, blank = True)
    top_seller = models.BooleanField(default = False)
    date_hired = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.name

