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
    

