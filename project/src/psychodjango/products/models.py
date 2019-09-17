from django.db import models

# Create your models here.

class Product(models.Model):

    nazwa = models.TextField()
    opis = models.TextField()
    cena = models.TextField()




