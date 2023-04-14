from django.db import models

# Create your models here.


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    author = models.TextField()
    inStock = models.BooleanField(default=True)
    genre = models.CharField(max_length=100)

