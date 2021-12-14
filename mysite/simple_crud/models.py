from django.db import models
import datetime

# Create your models here.


class Crud(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    