from django.urls import path
#from .views import product_list, contact, about
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

