from django.urls import path
from .views import *

app_name = "map"

urlpatterns = [
    path("<str:id>", map, name="map"),
]