from django.shortcuts import render, redirect, get_object_or_404
from .models import ComPost
from django.utils import timezone


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


def detail(request, id):
    post = get_object_or_404(ComPost, pk=id)
    return render(request, "community/detail.html", {"post": post})