from django.shortcuts import render, get_object_or_404, redirect
from community.models import ComPost
from posts.models import Post
from django.contrib.auth.models import User


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        "user": user,
        "ComPosts": ComPost.objects.filter(writer=user),
        "Posts" "followings": user.profile.followings.all(),
        "followers": user.profile.followers.all(),
    }
    return render(request, "users/mypage.html", context)


def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect("users:mypage", followed_user.id)


def edit(request):  # 개인만 쓸 페이지
    cur_user = request.user
    return render(request, "users/edit.html", {"user": cur_user})


def update(request):  # 개인만 쓸 함수
    update_profile = request.user.profile
    update_profile.name = request.POST["name"]
    update_profile.phnum = request.POST["phnum"]
    update_profile.address = request.POST["address"]
    update_profile.save()

    return redirect("users:mypage", request.user.id)


def user_posts(request, id):  # 다른 사람들도 접속하면 볼 수 있는 페이지(iframe)
    user = get_object_or_404(User, pk=id)
    context = {
        "user": user,
        "ComPosts": ComPost.objects.filter(writer=user),
        "Posts" "followings": user.profile.followings.all(),
        "followers": user.profile.followers.all(),
    }

    return render(request, "users/user_posts.html", context)


def introduce(request):  # 다른 사람들도 접속하면 볼 수 있는 페이지(iframe)
    return render(request, "introduce.html")