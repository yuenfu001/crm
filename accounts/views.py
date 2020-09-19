from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import OrderForm
# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    num_order = orders.count()
    total_customer = customers.count()
    total_order = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    content = {
        "customers": customers,
        "orders": orders,
        "total_order": total_order,
        "delivered": delivered,
        "pending": pending,
    }
    return render(request, "acct/dashboard.html", content)


def customer(request, pk):

    customer = Customer.objects.get(id=pk)

    order = customer.order_set.all()
    cus_order = order.count()
    context = {
        "customer": customer,
        "order": order,
        "cus_order": cus_order,
    }

    return render(request, "acct/customer.html", context)


def navbar(request):
    return render(request, "acct/navbar.html")


def products(request):
    products = Product.objects.all()

    return render(request, "acct/products.html", {"products": products})


def status(request):
    return render(request, "acct/status.html")

def createOrder(request):
    form = OrderForm 
    if request.method == "POST":
       # print("printing POST:",request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}
    return render(request, "acct/order_form.html", context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
       # print("printing POST:",request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form":form}
    return render(request,"acct/order_form.html",context )

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")

    context = {"item":order}
    return render(request,"acct/delete.html",context )