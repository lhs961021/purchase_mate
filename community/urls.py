from django.urls import path
from .views import *

app_name = "community"

urlpatterns = [
    path("new/", new, name="new"),
    path("create/", create, name="create"),
    path("<str:id>", detail, name="detail"),
]