from django.db import models

# Category model, each category has multiple books
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model, each book belongs to one category
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # ForeignKey creates a one-to-many relationship between Category and Book
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
