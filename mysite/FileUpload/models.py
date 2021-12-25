from django.db import models
import datetime
from .validators import validate_file_size

# Create your models here.


class FileUpload(models.Model):
	name = models.CharField(max_length=255)
	profile_pic = models.CharField(max_length=255)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)


class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', verbose_name="", validators=[validate_file_size])

    def __str__(self):
        return self.name + ": " + str(self.filepath)

