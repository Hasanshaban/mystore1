from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.
def get_image_path(id,brand):
    return os.path.join('photos',str(id),brand)


class Size(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Color(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='colors/',null=True)
    def __str__(self):
        return self.name

class Clothing(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image1=models.ImageField(upload_to='colors/',null=True)
    image2=models.ImageField(upload_to='colors/',null=True)
    image3=models.ImageField(upload_to='colors/',null=True)
    image4=models.ImageField(upload_to='colors/',null=True)
    #image=models.ManyToManyField('ImageModel',related_name='related_images',null=True)
    sizes=models.ManyToManyField(Size)
    color=models.ManyToManyField(Color)
    material=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    design=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=[('مردانه','مردانه'),('زنانه','زنانه')])
    def __str__(self):
        return self.name
class Size_info(models.Model):
    info=models.ForeignKey(Clothing,on_delete=models.CASCADE,null=True,max_length=100)
    name=models.ForeignKey(Size,on_delete=models.CASCADE,max_length=10)
    waist=models.IntegerField(null=True)
    seat=models.IntegerField(null=True)
    thigh=models.IntegerField(null=True)
    fagh=models.IntegerField(null=True)
    pants=models.IntegerField(null=True)
    def __str__(self):
        return str(self.name)    

class Order(models.Model):
    user=models.ForeignKey(User,max_length=100,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    product_name=models.ForeignKey(Clothing,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    delivery_address=models.TextField(max_length=100,default="خراسان رضوی-مشهد")
    phone_number=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ImageModel(models.Model):
    name=models.OneToOneField('Clothing',max_length=100,on_delete=models.CASCADE,null=True)
    name1=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to=get_image_path)
    

