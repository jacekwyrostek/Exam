from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls import include, url


urlpatterns = [
    url(r'search/', search, name='search'),
    url('studentExams/', studentExams, name='studentExams'),
    url('newQuestion/', newQuestion, name='newQuestion'),
    url('newExam/', newExam, name='newExam'),
    url('newQuestionSheet/', newQuestionSheet, name='newQuestionSheet'),
    url('questionSheet/<int:id>', questionSheet, name='questionSheet'),
    path('questionSheet/<int:id>', questionSheet, name='questionSheet'),
    #url('answerSheet/<int:id>', answerSheet, name='answerSheet'),
    path('answerSheet/<int:id>', answerSheet, name='answerSheet'),
    path('answer/<int:id>', editAnswer, name='answer')
]
