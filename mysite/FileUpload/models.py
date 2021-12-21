from django.db import models
import datetime

# Create your models here.


class FileUpload(models.Model):
	name = models.CharField(max_length=255)
	profile_pic = models.CharField(max_length=255)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
