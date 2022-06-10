from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('sales/', views.sales, name='sales'),
    path('combo/', views.combo, name='combo'),
    path('get_contact/', views.get_contact, name='get_contact_url')

]
