from django.shortcuts import render

def frontend(request):
    return render(request, 'blog/frontend.html', {})
