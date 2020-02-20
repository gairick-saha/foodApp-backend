from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('orderStatus/', views.status, name='Order Status'),
    path('search/', views.search, name='Search'),
    path('menuView/', views.menu, name='Menu View'),
    path('cart/', views.cart, name='Order Cart'),
    path('checkout/', views.checkout, name='Checkout'),
]
