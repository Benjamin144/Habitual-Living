from django.shortcuts import render

from .models import Post
posts = Post.objects.all()

def frontend(request):
    return render(request, 'blog/frontend.html', {'posts': posts})
