from .models import Product
from django.shortcuts import render, redirect
from .forms  import ContactForm
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect


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


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirige a la lista de productos después de guardar
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})