from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    amount = models.IntegerField()
    idCategory = models.IntegerField()