from django.contrib import admin
from app.models import Question, Answer, Questionnaire

__author__ = 'Administrator'


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Questionnaire)