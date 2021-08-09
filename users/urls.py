from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("<int:id>/mypage", mypage, name="mypage"),
    path("<int:id>/follow", follow, name="follow"),
    path("introduce/", introduce, name="introduce"),
    path("edit/", edit, name="edit"),
    path("update/", update, name="update"),
    path("<int:id>/posts", user_posts, name="user_posts"),
    path('<int:id>/follow_count/',follow_count,name="follow_count"),
]