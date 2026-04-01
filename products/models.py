from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50 , unique=True , null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
