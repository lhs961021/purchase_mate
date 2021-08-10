from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from community.models import ComPost
from posts.models import Post


def index(request):
    shop_follow = []
    shop_all = []
    if request.user.is_authenticated:
        user = request.user
        for friend in user.profile.followings.all():
            shop_follow += list(Post.objects.filter(writer=friend.user))
        shop_follow.sort(reverse=True, key=lambda x: x.pub_date)  # 최근 올라온 날짜대로 정렬
    shop_all += list(Post.objects.all())
    shop_all.sort(reverse=True, key=lambda x: x.pub_date)
    return render(
        request,
        "index.html",
        {"shop_follow": shop_follow[:4], "shop_all": shop_all[:4]},
    )
