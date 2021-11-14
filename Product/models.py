from datetime import datetime
from django.db import models
from django.forms.fields import CharField, DecimalField



# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    weight=models.DecimalField(max_digits=100,decimal_places=2)
    price=models.DecimalField(max_digits=100,decimal_places=2)
    created_at=models.DateTimeField(default=datetime.now())
    updated_at=models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.name