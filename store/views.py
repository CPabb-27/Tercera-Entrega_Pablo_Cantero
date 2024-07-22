from .models import Product
from .forms  import ContactForm
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import AssociateForm
from .models import Associate
from .models import Acreditation
from .forms import AcreditationForm
from store.models import UserProfile
from store.forms import UserProfileForm



def about(request):
    return render(request, 'store/about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            print(form.cleaned_data)  
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
            return redirect('product_list')  
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})


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

@login_required
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

def edit_associate(request, id):
    associate = get_object_or_404(Associate, id=id)

    if request.method == 'POST':
        associate.first_name = request.POST['first_name']
        associate.last_name = request.POST['last_name']
        associate.dni = request.POST['dni']
        associate.age = request.POST['age']
        associate.socio_type = request.POST['socio_type']
        associate.save()
        return redirect('associate')

    return render(request, 'store/edit_associate.html', {'associate': associate})

def delete_associate(request, id):
    associate = get_object_or_404(Associate, id=id)
    if request.method == 'POST':
        associate.delete()
        return redirect('associate')
    return render(request, 'store/confirm_delete.html', {'associate': associate})

@login_required
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

@login_required
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

@login_required
def delete_acreditation_view(request, pk):
    acreditation = get_object_or_404(Acreditation, pk=pk)
    if request.method == 'POST':
        acreditation.delete()
        return redirect('acreditation')
    return render(request, 'store/delete_acreditation.html', {'acreditation': acreditation})




@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'store/edit_profile.html', {'form': form})

def create_user_profile():
    users = User.objects.all()
    for user in users:
        if not hasattr(user, 'userprofile'):
            UserProfile.objects.create(user=user)

@login_required
def profile_view(request):
    user_profile = request.user.userprofile
    return render(request, 'store/profile.html', {'user_profile': user_profile})

