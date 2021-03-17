from django.shortcuts import render

# Create your views here.

def index(request):
    """ THIS view returns the index page OK """

    return render(request, 'landing/index.html')
