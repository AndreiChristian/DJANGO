from django.db import models

class Dough(models.Model):
    name = models.CharField(max_length=100)

class Topping(models.Model):
    name = models.CharField(max_length=100)

class Client(models.Model):
    name = models.CharField(max_length=100)

class Pizza(models.Model):
    dough = models.ForeignKey(Dough, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

