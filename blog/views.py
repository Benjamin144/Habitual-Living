from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post


def frontend(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontend.html', {'posts': posts})


def base(request):
    posts = Post.objects.all()

    return render(request, 'blog/base.html', {'posts': posts})



