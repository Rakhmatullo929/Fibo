from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(null=True)
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    category = models.ForeignKey('store.Category', default=None, on_delete=models.CASCADE)
    type = models.ForeignKey('store.Type', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.price}'

    class Meta:
        db_table = 'store_product'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'store_categories'


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'store_types'


class Slide(models.Model):
    image = models.ImageField(default='slide.jpg')


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class Sale(models.Model):
    image = models.FileField(null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    client_name = models.CharField(max_length=30, null=True)
    client_email = models.EmailField(null=True)
    client_number = models.CharField(max_length=30, null=True)

    def __str__(self):
        return F'{self.client_name} {self.client_email} {self.client_number}'
