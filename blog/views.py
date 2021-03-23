from django.shortcuts import render

from .models import Post
posts = Post.objects.all()

def frontend(request):
    return render(request, 'blog/frontend.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', {'post': post})
