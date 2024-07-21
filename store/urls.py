from django.urls import path
#from .views import product_list, contact, about
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path 
from store.views import * 
from django.contrib.auth.views import LogoutView,LoginView 
from .views import associate_view

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-product/', views.product_form, name='product_form'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.index, name='index'),
    path('associate/', associate_view, name='associate'),
    path('acreditation/', acreditation_view, name='acreditation'),
    path('acreditation/edit/<int:pk>/', edit_acreditation_view, name='edit_acreditation'),
]

