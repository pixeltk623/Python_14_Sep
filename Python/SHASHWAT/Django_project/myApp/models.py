from django.db import models


class Crud(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, default=True)
    hobbies = models.CharField(max_length=255, default=True)
    cityName = models.CharField(max_length=255, default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    