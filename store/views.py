from .models import Product
from django.shortcuts import render, redirect
from .forms  import ContactForm
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import AssociateForm
from .models import Associate
from .models import Acreditation
from .forms import AcreditationForm

def about(request):
    return render(request, 'store/about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            print(form.cleaned_data)  # Imprime los datos del formulario en la consola
            return redirect('contact')  
    else:
        form = ContactForm()

    return render(request, 'store/contact.html', {'form': form})


def cart(request):
    return render(request, 'store/cart.html')


def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)
   
    return redirect('product_list')

@login_required
def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirige a la lista de productos después de guardar
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})

#@login_required
#def asociarme(request):
#    return render(request, 'store/asociarme.html')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list') 
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def index(request):
    return render(request, 'store/base.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            login(request, user)
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def associate_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dni = request.POST['dni']
        age = request.POST['age']
        socio_type = request.POST['socio_type']
        Associate.objects.create(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            age=age,
            socio_type=socio_type
        )
        return redirect('associate')
    
    associates = Associate.objects.all()
    return render(request, 'store/associate.html', {'associates': associates})

def acreditation_view(request):
    if request.method == 'POST':
        form = AcreditationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acreditation')
    else:
        form = AcreditationForm()
    acreditations = Acreditation.objects.all()
    return render(request, 'store/acreditation.html', {'form': form, 'acreditations': acreditations})

def edit_acreditation_view(request, pk):
    acreditation = get_object_or_404(Acreditation, pk=pk)
    if request.method == 'POST':
        form = AcreditationForm(request.POST, instance=acreditation)
        if form.is_valid():
            form.save()
            return redirect('acreditation')
    else:
        form = AcreditationForm(instance=acreditation)
    return render(request, 'store/edit_acreditation.html', {'form': form})