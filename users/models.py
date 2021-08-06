from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="")
    phnum = models.CharField(max_length=12)
    address = models.CharField(max_length=200, default="")