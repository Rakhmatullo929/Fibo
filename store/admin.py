from django.contrib import admin
from store.models import *

admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Type),
admin.site.register(Slide),
admin.site.register(CartItem),
admin.site.register(Sale),