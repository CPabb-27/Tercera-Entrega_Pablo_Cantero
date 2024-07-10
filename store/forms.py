from django import forms
from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'description', 'stock']