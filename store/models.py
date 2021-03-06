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

    def desk(self):
        return f'{self.description[:30]}'

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


SIZE_CHOICES = [
    ('Маленькая', 'Маленькая'),
    ('Средняя', 'Средняя'),
    ('Большая', 'Большая')
]

THICKNESS_CHOICES = [
    (1, 'Традиционное'),
    (2, 'Тонкое'),
]


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(choices=SIZE_CHOICES, max_length=30, null=True, blank=True)
    thickness = models.PositiveIntegerField(choices=THICKNESS_CHOICES, null=True, blank=True)

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


class Order(models.Model):
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    total_price = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Order # %s' % (str(self.id))


# class OrderProduct(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     order = models.ForeignKey('store.Order', on_delete=models.CASCADE, related_name='order_products')
#     product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     total = models.IntegerField()
#
#     def str(self):
#         return '%s x%s - %s' % (self.product, self.amount, self.order)


class OrderProduct(models.Model):
    order = models.ForeignKey('store.Order', on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '%s x%s - %s' % (self.product, self.amount, self.order.customer.username)
