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


