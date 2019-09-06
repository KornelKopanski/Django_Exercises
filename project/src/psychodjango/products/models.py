from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=120) #maksymalna ilość znaków
    description = models.TextField(blank=True,null=True) # w tym momencie wpisywanie opisu nie jest konieczne
    price = models.DecimalField(max_digits=10000,decimal_places=2) # max_digits - maksymalna cena, decimal_places - miejsca po przecinku
    summary = models.TextField(default= 'Django jest ok')
    discount = models.BooleanField()


