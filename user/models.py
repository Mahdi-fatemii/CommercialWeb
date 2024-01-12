from django.contrib.auth.validators import *
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=500)
    mobile_number = models.CharField(max_length=11, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "address", "mobile_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class User(AbstractUser):
#
#     def __str__(self):
#         return "{}".format(self.email)
#
#     username = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=2000)
#     first_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)
#     email = models.EmailField(unique=True, default='test@test.com')
#     address = models.CharField(max_length=500)
#     mobile_number = models.CharField(max_length=11, unique=True, default='09*********')
#     date_joined = models.DateTimeField("date joined", default=timezone.now)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name', "password", "address", "mobile_number", "email"]
