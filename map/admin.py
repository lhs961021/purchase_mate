from posts.models import Post
from django.contrib import admin
from .models import Search

# Register your models here.
admin.site.register(Search)
admin.site.register(Post)
