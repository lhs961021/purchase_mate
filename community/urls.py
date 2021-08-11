from django.urls import path
from .views import *

app_name = "community"

urlpatterns = [
    path("", community, name="community"),
    path("<str:id>", detail, name="detail"),
    path("new/", new, name="new"),
    path("create/", create, name="create"),
    path("edit/<str:id>", edit, name="edit"),
    path("update/<str:id>", update, name="update"),
    path("delete/<str:id>", delete, name="delete"),
    path("<str:post_id>/create_comment", create_comment, name="create_comment"),
    path("edit_comment/<str:id>", edit_comment, name="edit_comment"),
    path("update_comment/<str:id>", update_comment, name="update_comment"),
    path("delete_comment/<str:id>", delete_comment, name="delete_comment"),
]