from django.db import models  #py manage.py startapp service  for creating app for model model
class Service(models.Model):  #py manage.py makemigrations for creating schema
    service_icon=models.CharField(max_length=50)      #py manage.py migrate for creating table
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()

# Create your models here.
