from datetime import datetime
from statistics import mode
from django.db import models


# Create your models here.
class FashionJewellery(models.Model):    
    Title=models.CharField(max_length=100)
    Price = models.IntegerField()
    Image_main = models.ImageField(upload_to='images/FashionJewellery')
    Image_1 = models.ImageField(upload_to='images/FashionJewellery', blank=True)
    Image_2 = models.ImageField(upload_to='images/FashionJewellery', blank=True)
    Image_3 = models.ImageField(upload_to='images/FashionJewellery', blank=True)
    Image_4 = models.ImageField(upload_to='images/FashionJewellery', blank=True)
    Image_5 = models.ImageField(upload_to='images/FashionJewellery', blank=True)
    Image_6 = models.ImageField(upload_to='images/FashionJewellery', blank=True)
    type = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id) + " "+ self.Title

class PreciousJewellery(models.Model):
    Title=models.CharField(max_length=100)
    Price = models.IntegerField()
    Image_main = models.ImageField(upload_to='images/PreciousJewellery')
    Image_1 = models.ImageField(upload_to='images/PreciousJewellery', blank=True)
    Image_2 = models.ImageField(upload_to='images/PreciousJewellery', blank=True)
    Image_3 = models.ImageField(upload_to='images/PreciousJewellery', blank=True)
    Image_4 = models.ImageField(upload_to='images/PreciousJewellery', blank=True)
    Image_5 = models.ImageField(upload_to='images/PreciousJewellery', blank=True)
    Image_6 = models.ImageField(upload_to='images/PreciousJewellery', blank=True)
    type = models.CharField(max_length=30)
    Metal = models.CharField(max_length=10)
    desc = models.CharField(max_length=50)
    def __str__(self):
        return  str(self.id) +" "+ self.Title




class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email =  models.CharField(max_length=90)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=12)
    amount =models.IntegerField()
    paymentmethod = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now)
    SKU = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    query = models.TextField()

    def __str__(self):
        return self.name