from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q


@login_required(login_url='/users/sign_in')
def home(request):
    product_id = request.GET.get('product')
    category = request.GET.get('category')
    type = request.GET.get('type')
    products = Product.objects.all()
    slides = Slide.objects.all()
    if product_id:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(customer=request.user, product=product, quantity=1)
            cart_item.save()
            return redirect('store:home')
        for item in cart_item:
            item.quantity += 1
            item.save()
    products = products.filter(category=category) if category else products
    products = products.filter(type=type) if type else products
    return render(request, 'home.html', {'products': products, 'slides': slides})


def contact(request):
    contact = Product.objects.all
    return render(request, 'contact.html', {'contact': contact})


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(request, 'cart.html',
                  {'cart_items': cart_items,
                   'total_quantity': total_quantity,
                   'total_price': total_price},
                  )


def sales(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})


def combo(request):
    return render(request, 'combo.html')


def get_contact(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    telephone = request.GET.get('telephone')
    Feedback.objects.create(
        client_name=name,
        client_email=email,
        client_number=telephone
    )
    return redirect('store:home')