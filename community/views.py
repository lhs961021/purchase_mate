from django.shortcuts import render, redirect, get_object_or_404
from .models import ComPost
from django.utils import timezone


def community(request):
    posts = ComPost.objects.all()
    return render(request, "community/community.html", {"posts": posts})


def detail(request, id):
    post = get_object_or_404(ComPost, pk=id)
    return render(request, "community/detail.html", {"post": post})


def new(request):
    return render(request, "community/new.html")


def create(request):
    new_post = ComPost()
    new_post.title = request.POST["title"]
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST["body"]
    new_post.image = request.FILES.get("image")
    new_post.save()
    return redirect("community:detail", new_post.id)


def edit(request, id):
    edit_post = ComPost.objects.get(id=id)
    return render(request, "community/edit.html", {"post": edit_post})


def update(request, id):
    update_post = ComPost.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST["body"]
    update_post.image = request.FILES.get("image")
    update_post.save()
    return redirect("community:detail", update_post.id)


def delete(request, id):
    delete_post = ComPost.objects.get(id=id)
    delete_post.delete()
    return redirect("community:community")