from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    size = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    


