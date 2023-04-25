from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(
        Subcategory, related_name="items", on_delete=models.CASCADE)
