# Generated by Django 4.0 on 2021-12-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_crud_cityname_crud_hobbies'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='profile_pic',
            field=models.CharField(default=True, max_length=255),
        ),
    ]