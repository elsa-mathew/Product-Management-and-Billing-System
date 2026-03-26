from django.db import models
from products.models import Product

class Inventory(models.Model):

    product = models.OneToOneField(Product , on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def stock(self):
        if self.quantity<0:
            raise ValidationError("Stock cannot be negative")

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
