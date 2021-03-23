from django.shortcuts import render

from .models import Post


def frontend(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontend.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', {'post': post})
