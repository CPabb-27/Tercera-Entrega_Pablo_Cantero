from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Associate
from .models import Acreditation

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'description', 'stock']

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requerido.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class AssociateForm(forms.ModelForm):
    class Meta:
        model = Associate
        fields = ['first_name', 'last_name', 'dni', 'age', 'socio_type']

class AcreditationForm(forms.ModelForm):
    class Meta:
        model = Acreditation
        fields = ['name', 'surname', 'email', 'address', 'address_number', 'media_outlet']