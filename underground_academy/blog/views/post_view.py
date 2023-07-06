from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime

def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog/blog.html", {"posts": posts, "total_posts": total_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_detail.html", {"post": post})
