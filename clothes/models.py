from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.

class Clothing(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image1=models.ImageField(upload_to='colors/',null=True)
    def __str__(self):
        return self.name


