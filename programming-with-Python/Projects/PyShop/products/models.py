from django.db import models


class Product(models.Model):
    name : str = models.CharField(max_length=255)
    price : float = models.DecimalField(max_digits=10, decimal_places=2)
    stock : int = models.IntegerField(default=0)
    image_url : str = models.CharField(max_length=2083)
