from django.db import models
from django.contrib.auth.models import User as Use
from django.contrib.auth.validators import *
from django.utils import timezone
from django.contrib.auth import hashers
import bcrypt

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=2000)
    name = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, default='test@test.com')
    address = models.CharField(max_length=500)
    mobile_number = models.CharField(max_length=11, unique=True, default='09*********')
    date_joined = models.DateTimeField("date joined", default=timezone.now)


