from django.shortcuts import render, redirect, get_object_or_404
from .models import ComPost, Comment
from django.utils import timezone


def community(request):
    if request.user.is_authenticated:
        posts = ComPost.objects.all()
        return render(request, "community/community.html", {"posts": posts})
    else:
        return redirect("account_login")


def detail(request, id):
    post = get_object_or_404(ComPost, pk=id)
    all_comments = post.comments.all().order_by("-created_at")
    return render(
        request, "community/detail.html", {"post": post, "comments": all_comments}
    )


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
    if request.FILES.get('image'):
        update_post.image=request.FILES.get('image')
    update_post.save()
    return redirect("community:detail", update_post.id)


def delete(request, id):
    delete_post = ComPost.objects.get(id=id)
    delete_post.delete()
    return redirect("community:community")


def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(ComPost, pk=post_id)
        current_user = request.user
        comment_content = request.POST.get("content")
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect("community:detail", post_id)


def edit_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        return render(request, "community/edit_comment.html", {"comment": comment})
    else:
        return redirect("community:detail", comment.post.id)


def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.content = request.POST.get("content")
    comment.save()
    return redirect("community:detail", comment.post.id)


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        comment.delete()
    return redirect("community:detail", comment.post.id)
