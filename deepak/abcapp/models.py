from django.db import models
from django.contrib import admin


class mechshop_DB(models.Model):

    phone = models.CharField(max_length=10)
    date = models.DateField()
    vehicle_no = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=10)
    bike_name = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.TextField()


class mechshop_DBAdmin(admin.ModelAdmin):
    list_display = ["phone", "date", "vehicle_no", "Name", "bike_name", "Email", "Address"]