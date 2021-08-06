from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class ComPost(models.Model):  # 일반 커뮤니티용 모델
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="post/", null=True, blank=True)