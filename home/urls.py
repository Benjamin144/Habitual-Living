# https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware #

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
