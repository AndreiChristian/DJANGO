from django.db import models

# Create your models here.
# class Book(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True)
#     price = models.IntegerField()
#     description = models.TextField()
#     author = models.TextField()
#     inStock = models.BooleanField(default=True)
#     genre = models.CharField(max_length=100)


class FacilityItem(models.Model):

    facility_item_level_choices = [
        ("G", "Guest"),
        ("R", "Room"),
        ("P", "Property")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    imagePath = models.TextField()
    level = models.CharField(max_length=2, choices=facility_item_level_choices)
    included = models.BooleanField(default=True)
    extraPrice = models.IntegerField(default=0)


class FacilityGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    facility_items = models.ManyToManyField(FacilityItem)

    def __str__(self):
        return self.name
