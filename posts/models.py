from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from django.db.models.deletion import CASCADE

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)  # 수정한 후에 업로드시간 및 날짜 변하지 않게 다시 수정할 것!
    deadline = models.DateField(auto_now=False)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    people = models.IntegerField(default=0, null=True)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    chat = models.CharField(max_length=200, null=True)
    spot = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

class Spot(models.Model):
    spot = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.spot

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address