from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Admin)
admin.site.register(Product)
admin.site.register(UsedProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(CartProduct)
admin.site.register(Category)
admin.site.register(ProductImage)
