# Create your models here.

from django.db import models
import uuid


class Order(models.Model):
    # In this example, I'll use UUIDs for primary keys
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    customer = models.CharField(max_length=256, blank=False, null=False)

    address = models.CharField(max_length=512, blank=True, null=False)


class Box(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    color = models.CharField(
        max_length=32, default="white", blank=False, null=False
    )


class Topping(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=64
    )


class Pizza(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    order = models.ForeignKey(
        "pizzaria.Order",
        on_delete=models.CASCADE,
        related_name="pizzas",
        null=False
    )

    box = models.OneToOneField(
        "pizzaria.Box",
        on_delete=models.SET_NULL,
        related_name="contents",
        null=True
    )

    toppings = models.ManyToManyField(
        "pizzaria.Topping",
        related_name='+'
    )
