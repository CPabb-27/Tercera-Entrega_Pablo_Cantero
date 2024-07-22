
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Descripción no disponible')  # Valor predeterminado
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name



class Associate(models.Model):
    SOCIO_CHOICES = [
        ('socio_activo', 'Socio Activo'),
        ('socio_cadete', 'Socio Cadete'),
        ('socio_menor', 'Socio Menor'),
        ('socio_interior_pais', 'Socio Interior País'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    age = models.IntegerField()
    socio_type = models.CharField(max_length=20, choices=SOCIO_CHOICES)

    
class Acreditation(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    direccion_domicilio = models.CharField(max_length=255)
    numero_domicilio = models.CharField(max_length=10)
    medio_televisivo = models.CharField(max_length=255, default='N/A')  # Valor predeterminado

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username