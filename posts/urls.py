from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path("", shop, name="shop"),
    path("shop_detail/", shop_detail, name="shop_detail"),
]