from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description')

# Asegúrate de que solo hay un registro del modelo Product
admin.site.register(Product, ProductAdmin)
