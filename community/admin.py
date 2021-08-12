from community.models import ComPost, Comment
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ComPost)
admin.site.register(Comment)