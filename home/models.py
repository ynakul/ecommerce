from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,default="")
    full_name = models.CharField(max_length=60 ,default="")
    image = models.ImageField(upload_to="admins")
    mobile = models.CharField(max_length=20 ,default="")

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,default="")
    full_name = models.CharField(max_length=200 ,default="")
    address = models.CharField(max_length=200, null=True, blank=True ,default="")
    joined_on = models.DateTimeField(auto_now_add=True)
    phone=models.PositiveIntegerField(default=0 ,max_length=10)

    def __str__(self):
        return self.full_name

class Profile(models.Model):
    user = models.OneToOneField(Customer ,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)

class Category(models.Model):
    title = models.CharField(max_length=200 ,default="")
    
    


    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=200 ,default="")
    product_type=models.CharField(max_length=300, null=True, blank=True ,default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    condition = models.CharField(max_length=300, null=True, blank=True ,default="")
    language= models.CharField(max_length=300, null=True, blank=True ,default="")
    price_range= models.CharField(max_length=300, null=True, blank=True ,default="")
    binding= models.CharField(max_length=300, null=True, blank=True ,default="")
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    description = models.TextField(default="")
    warranty = models.CharField(max_length=300, null=True, blank=True ,default="")
    return_policy = models.CharField(max_length=300, null=True, blank=True ,default="")
    view_count = models.PositiveIntegerField(default=0)
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();
    
    def __str__(self):
        return self.title

    

class UsedProduct(models.Model):
    title = models.CharField(max_length=200 ,default="")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    description = models.TextField(default="")
    warranty = models.CharField(max_length=300, null=True, blank=True ,default="")
    return_policy = models.CharField(max_length=300, null=True, blank=True ,default="")
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    subtotal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200 ,default="")
    shipping_address = models.CharField(max_length=200 ,default="")
    mobile = models.CharField(max_length=10 ,default="")
    email = models.EmailField(null=True, blank=True ,default="")
    subtotal = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS ,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)

