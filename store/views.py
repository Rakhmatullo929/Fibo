from django.shortcuts import render, redirect

# Create your views here.
from .forms import RateForm
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
    contact = Product.objects.all()
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


def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()
    return redirect('store:cart')


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('store:cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('store:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('store:cart')


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


def create_order(request):
    cart_items = CartItem.objects.all()
    total_price = sum([item.total_price() for item in cart_items])
    amount = sum([item.quantity for item in cart_items])
    form = forms.OrderForm(request.POST)

    print(request.method)

    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(
            customer=request.user,
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            total_price=total_price,
        )
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.quantity,
                total=cart_item.total_price(),
            )

        cart_items.delete()
        return redirect('store:order_success')
    form = forms.OrderForm()
    return render(request, 'create_order.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'amount': amount,
        'form': form
    })


def order_success(request):
    return render(request, 'order_success.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    cart_item = CartItem.objects.filter(customer=request.user, product=product)
    if not cart_item and request.method == 'POST':
        form_rating = CartItem.objects.create(
            customer=request.user,
            product=product,
            quantity=1,
            size=request.POST.get('size'),
            thickness=request.POST.get('thickness'),
        )
        form_rating.save()
        return redirect('store:home')
    if cart_item and request.method == 'POST':
        quantity = 0
        for item in cart_item:
            quantity = item.quantity + 1
        CartItem.objects.update(
            quantity=quantity,
            size=request.POST.get('size'),
            thickness=request.POST.get('thickness'),
        )
        return redirect('store:home')
    form_rating = RateForm()
    return render(request, 'product_detail.html',
                  {'product': product,
                   'form_rating': form_rating, }
                  )
