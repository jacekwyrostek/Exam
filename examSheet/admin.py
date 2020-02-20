from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('question',)

@admin.register(QuestionSheet)
class QuestionSheetAdmin(admin.ModelAdmin):
    list_display=('examName', 'owner')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display=('exam', 'question', 'answer', 'student', 'note')

@admin.register(AnswerSheet)
class AnswerSheetAdmin(admin.ModelAdmin):
    list_display=('exam', 'student', 'note')
