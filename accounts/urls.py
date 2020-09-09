from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("customer/", views.customer, name="cus"),
    path("navbar/", views.navbar, name="nav"),
    path("products/", views.products, name="prod"),
    path("status/", views.status, name= "status"),
]
