from django.db import models



class Product(models.Model):

    nazwa = models.CharField(max_length=120)
    opis = models.TextField(blank=True,null=True)
    cena = models.DecimalField(max_digits=10000,decimal_places=2)
    podsumowanie = models.TextField(default='Django jest naprawdę fajny')
