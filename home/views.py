# https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware #

from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
