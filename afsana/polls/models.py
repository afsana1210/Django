from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone



class signup(models.Model):
    first_name=models.CharField(max_length=50)
    second_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=140,default='enter email')
    password=models.CharField(max_length=50)

class signin(models.Model):
    email=models.EmailField(max_length=140,default='enter email')
    password=models.CharField(max_length=50)

# from django.db import models
# from django_google_maps import fields as map_fields

# class Rental(models.Model):
#     address = map_fields.AddressField(max_length=200)
#     geolocation = map_fields.GeoLocationField(max_length=100)


