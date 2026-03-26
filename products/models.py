from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50 , unique=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
