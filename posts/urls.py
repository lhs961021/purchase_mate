from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path("",shop, name="shop"),
    path("shop_detail/",shop_detail, name="shop_detail"),
    #정렬부분
    path("recent_postlist/",recent_postlist,name="recent_postlist"),
    path("all_postlist/",all_postlist,name="all_postlist"),
    path("deadline_postlist/",deadline_postlist,name="deadline_postlist"),
    path("distance_postlist/",distance_postlist,name="distance_postlist"),
    path("price_postlist/",price_postlist,name="price_postlist"),
    #CRUD부분
    path("makepost/",makepost,name="makepost"),
    path("<str:id>",detail,name="detail"),
    path("create/",create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>',update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    #카테고리부분
    path('category/food/',food,name="food"),
    path('category/daily_necessity/',daily_necessity,name="daily_necessity"),
    path('category/ott/',ott,name="ott"),
    path('category/etc/',etc,name="etc"),
    #검색
    path('result/',result,name="result"),
]