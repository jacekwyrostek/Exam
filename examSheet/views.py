from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def search(request):
    list=[]
    search=SearchForm(request.POST or None, request.FILES or None)
    if search.is_valid():
        exam=int(search.cleaned_data['exam'])
        list=Answer.objects.filter(exam=exam, student=request.user)
    context={
    'search':search,
    'list':list
    }
    return render(request, 'search.html', context)


def studentExams(request):
    examList=QuestionSheet.objects.filter(student=request.user)
    context={
    'examList':examList
    }
    return render(request, 'list.html', context)
