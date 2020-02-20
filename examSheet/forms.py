from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404, render_to_response


class SearchForm(forms.Form):
    owner=forms.ModelChoiceField(queryset=User.objects.filter(groups__name='owner'))
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question']

class newQuestionSheetForm(forms.ModelForm):
    question=forms.ModelMultipleChoiceField(queryset=Question.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=True)
    class Meta:
        model = QuestionSheet
        fields=['examName', 'owner']

class newQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['question']

class newExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields=['name']
