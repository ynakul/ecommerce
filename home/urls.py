from django.contrib import admin
from django.urls import path
from django import views
from django.urls.conf import include
from home import views
import home 
from .views import *



def new_func():
    return path
app_name = "books"
urlpatterns = [
    path("",  indexView.as_view(), name="index"),
    path("about", views.about , name='about'),
    path("howitworks", views.howitworks , name='howitworks'),
   path("category/", views.category, name="category"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("addtocart/<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    
    path("mycart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("register/",
         CustomerRegistrationView.as_view(), name="customerregistration"),
    

    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("forgot-password/", PasswordForgotView.as_view(), name="passworforgot"),
    path("password-reset/<email>/<token>/",
         PasswordResetView.as_view(), name="passwordreset"),
    path("search/", SearchView.as_view(), name="search"),
    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),
    path("sell/", SellView.as_view(), name="sell"),

   # Admin Side pages

    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),

    path("admin-order-<int:pk>-change/",
         AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),

    path("admin-product/list/", AdminProductListView.as_view(),
         name="adminproductlist"),
    path("admin-product/add/", AdminProductCreateView.as_view(),
         name="adminproductcreate"),


]