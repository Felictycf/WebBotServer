from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)


class KeSuanInfo(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    age = models.IntegerField(default=2)
    number = models.CharField(max_length=64)
    jiating = models.CharField(max_length=64)
    vaccine = models.CharField(max_length=64)
    kesuan= models.CharField(max_length=64)
    jinzhu = models.CharField(max_length=64)
    # date = models.DateField(auto_now_add=False)


class ShopInfo(models.Model):
    name = models.CharField(max_length=32)
    dange = models.CharField(max_length=32)
    status= models.CharField(max_length=64)


class jinhuoINFo(models.Model):
    name = models.CharField(max_length=32)
    factory = models.CharField(max_length=32)
    shopId = models.IntegerField(default=2)
    number = models.CharField(max_length=64)
    sum = models.CharField(max_length=64)


class kuchunINfo(models.Model):
    name = models.CharField(max_length=32)
    sum = models.CharField(max_length=64)
    status= models.CharField(max_length=64)

