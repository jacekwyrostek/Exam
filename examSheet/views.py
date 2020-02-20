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
@permission_required
def newExam(request):
    form=newExamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(newQuestionSheet)
    context={'form':form}
    return render(request, 'newQuestionSheet.html', context)

#Add new question
@permission_required
def newQuestion(request):
    form=newQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(newQuestionSheet)
    context={'form':form}
    return render(request, 'newQuestionSheet.html', context)

#Add new question sheet
@permission_required
def newQuestionSheet(request):
    form=newQuestionSheetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(search)
    context={'form':form}
    return render(request, 'newQuestionSheet.html', context)

#Create Answer Sheet based on question sheet
@permission_required
def questionSheet(request, id):
    sheet=QuestionSheet.objects.get(pk=id)
    name=sheet.examName
    questions=sheet.questions
    if  AnswerSheet.objects.filter(exam=name, student=request.user).exists():
        id=AnswerSheet.objects.get(exam=name, student=request.user).id
    else:
        answerSheet=AnswerSheet(exam=name, student=request.user)
        answerSheet.save()
        question=sheet.questions.values_list('id', flat=True)
        for q in question:
            question=Question.objects.get(id=q)
            answer=Answer(exam=name, question=q, student=request.user)
            answer.save()
            answerSheet.answers.add(Answer.id)
            answerSheet.save()
    answerSheet=AnswerSheet.objects.get(exam=name, student=request.user)
    context={
        'sheet':sheet,
        'name':name,
        'questions':questions,
        'answerSheet':answerSheet,
    }
    return render(request, 'QuestionSheet.html', context)


def answerSheet(request, id):
    aSheet=AnswerSheet.objects.get(pk=id)
    context={
        'aSheet':aSheet,
    }
    return render(request, 'answerSheet.html', context)

#Edit answer text
@permission_required
def editAnswer(request, id):
    answer=get_object_or_404(Answer, pk=id)
    form=editAnswerForm(request.POST or None, instance=answer)
    answerSheetID=AnswerSheet.objects.get(exam=answer.exam, student=answer.student)
    if form.is_valid():
        form.save()
        return redirect('answerSheet', id=answerSheetID.id)
    context={
        'form':form,
        'answer':answer,
    }
    return render(request, 'answer.html', context)
