from django.db import models


class Product(models.Model):
    name : str = models.CharField(max_length=255)
    price : float = models.DecimalField(max_digits=10, decimal_places=2)
    stock : int = models.IntegerField(default=0)
    image_url : str = models.CharField(max_length=2083)


class Offer(models.Model):
    code : str = models.CharField(max_length=100)
    description : str = models.CharField(max_length=50)
    discount : float = models.DecimalField(max_digits=10, decimal_places=2)