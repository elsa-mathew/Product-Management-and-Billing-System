from django.db import models
from products.models import Product
from inventory.models import Inventory
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Bill(models.Model):
    created_by = models.ForeignKey(User , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)

    def __str__(self):
        return f"Bill {self.id} - {self.total}"

class BillItem(models.Model):
    bill = models.ForeignKey(Bill , on_delete = models.CASCADE , related_name = 'items')
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def save(self, *args, **kwargs):

    
        try:                                                                    #get inventory
            inventory_obj = Inventory.objects.get(product=self.product)
        except Inventory.DoesNotExist:
            raise ValidationError("Inventory not found")

      
        if self.quantity <= 0:                                                  #validation
            raise ValidationError("Quantity must be greater than 0")

        if self.quantity > inventory_obj.quantity:
            raise ValidationError("Not enough stock")

    
        self.price = self.product.price

    
        inventory_obj.quantity -= self.quantity                                  #reduce inventory
        inventory_obj.save()

    
        super().save(*args, **kwargs)                                            #save bill item
        

    def __str__(self):
        return f"{self.product.name} - ({self.quantity})"
