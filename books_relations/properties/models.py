from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FacilityCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FacilitySubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        FacilityCategory, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name


class FacilityItem(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(
        FacilitySubCategory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    square_meters = models.IntegerField()
    facility_categories = models.ManyToManyField(FacilityCategory)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='reservations')
    users = models.ManyToManyField(User, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Reservation {self.id} at {self.property}"
