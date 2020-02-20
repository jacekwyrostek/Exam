from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
def search(request):
    list=[]
    search=SearchForm(request.POST or None)
    if search.is_valid():
        owner=search.cleaned_data['owner']

        list=QuestionSheet.objects.filter(owner=owner)
    context={
    'search':search,
    'list':list
    }
    return render(request, 'search.html', context)


def studentExams(request):
    examList=QuestionSheet.objects.filter(owner=request.user)
    context={
    'examList':examList,
    }
    return render(request, 'examList.html', context)

#Add new exam model
def newExam(request):
    form=newExamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(newQuestionSheet)
    context={'form':form}
    return render(request, 'newQuestionSheet.html', context)
#Add ne question
def newQuestion(request):
    form=newQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(newQuestionSheet)
    context={'form':form}
    return render(request, 'newQuestionSheet.html', context)


def newQuestionSheet(request):
    form=newQuestionSheetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(search)
    context={'form':form}
    return render(request, 'newQuestionSheet.html', context)

def questionSheet(request, id):
    sheet=QuestionSheet.objects.get(pk=id)
    name=sheet.examName
    questions=sheet.questions
    context={
    'sheet':sheet,
    'name':name,
    'questions':questions
    }
    return render(request, 'QuestionSheet.html', context)
