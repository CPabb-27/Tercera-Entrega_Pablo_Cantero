#from django.db import models
#
#class Product(models.Model):
#    name = models.CharField(max_length=200)
#    price = models.DecimalField(max_digits=10, decimal_places=2)
#    stock = models.IntegerField()  # Asegúrate de que este campo esté definido
#    image = models.ImageField(upload_to='images/')
#
#    def __str__(self):        
#        return self.name
#
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Descripción no disponible')  # Valor predeterminado
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
