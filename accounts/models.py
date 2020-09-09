from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=70, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):

    CAT = (
        ("Indoors", "Indoors"),("Out", "Out door"),
    )
    name = models.CharField(max_length=20, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=7, null=True, choices=CAT)
    description = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    STATUS = (
        ("Delivered", "Delivered"),
        ("Out for delivery", "Out for delivery"),
        ("Pending", "Pending"),
    )

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS, default="Delivered")
    

    def __str__(self):
        return f"{self.customer} {self.product} {self.status}"

    # LOAN STATUS is a called a tuple