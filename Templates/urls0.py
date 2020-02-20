from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls import include, url


urlpatterns = [
    url(r'search/', search, name='search'),
    url('studentExams/', studentExams, name='studentExams'),
    url('newQuestionSheet/', newQuestionSheet, name='newQuestionSheet'),
    url('newQuestion/', newQuestion, name='newQuestion'),
    url('newExam/', newExam, name='newExam'),

]
