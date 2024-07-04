from .models import Product
from django.shortcuts import render, redirect
from .forms  import ContactForm


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
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)
   
    return redirect('product_list')
