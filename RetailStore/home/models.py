from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    Contact = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)

class Order(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='BillingTo')
    Time = models.DateTimeField(auto_now_add=True, editable=False)
    TotalAmount = models.IntegerField()

class Product(models.Model):
    ProductID = models.IntegerField()
    Name = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Cost = models.IntegerField()
    FinalCost = models.IntegerField()
    orders = models.ManyToManyField(Order)
