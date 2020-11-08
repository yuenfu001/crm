from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("customer/<str:pk>/", views.customer, name="cus"),
    path("navbar/", views.navbar, name="nav"),
    path("products/", views.products, name="prod"),
    path("status/", views.status, name= "status"),
    path("order/", views.createOrder, name = "order"),
    path("update/<str:pk>/", views.updateOrder, name ="update"),
    path("delete/<str:pk>", views.deleteOrder, name = "delete"),
    
]
