from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_shop = models.BooleanField('Shop', default=False)
    is_customer = models.BooleanField('Customer', default=False)


class Shop(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    shop_name = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    category = models.CharField(max_length=200, default='')
    contact_person = models.CharField(max_length=200, default='')
    branded = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    password2 = models.CharField(max_length=200, default='')


class Product(models.Model):
    product_name = models.CharField(max_length=200, default='')
    price = models.IntegerField()
    discount = models.IntegerField()


class Offer(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    shop_name = models.CharField(max_length=200, default='')
    image = models.ImageField(default='kg.jpg', null=True, upload_to='image/')
    offer_name = models.CharField(max_length=200, default='')
    valid_from = models.CharField(max_length=200, default='')
    valid_till = models.CharField(max_length=200, default='')
    discount = models.CharField(max_length=200, default='')

