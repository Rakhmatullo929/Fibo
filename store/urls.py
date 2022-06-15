from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('sales/', views.sales, name='sales'),
    path('combo/', views.combo, name='combo'),
    path('get_contact/', views.get_contact, name='get_contact_url'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success')
]
