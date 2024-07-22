from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path 
from store.views import * 
from django.contrib.auth.views import LogoutView,LoginView 
from .views import associate_view
from .views import acreditation_view, edit_acreditation_view
from django.conf import settings

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
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('associate/edit/<int:id>/', views.edit_associate, name='edit_associate'),
    path('associate/delete/<int:id>/', views.delete_associate, name='delete_associate'),
    path('acreditation/', views.acreditation_view, name='acreditation'),
    path('acreditation/edit/<int:pk>/', views.edit_acreditation_view, name='edit_acreditation'),
    path('acreditation/delete/<int:pk>/', views.delete_acreditation_view, name='delete_acreditation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

