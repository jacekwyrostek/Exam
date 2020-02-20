from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question=models.CharField(max_length=150)
    def __str__(self):
        return self.question

class Exam(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name

class QuestionSheet(models.Model):
    examName=models.ForeignKey(Exam, on_delete=models.CASCADE)
    questions=models.ManyToManyField(Question)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.examName)

class Answer(models.Model):
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    answer=models.CharField(max_length=150, blank=True, null=True)
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    note=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.question.question

class AnswerSheet(models.Model):
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)
    answers=models.ManyToManyField(Answer)
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    note=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.exam.name
