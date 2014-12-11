#coding:utf-8

from django.db import models

# Create your models here.

class Answer(models.Model):
    class Meta:
        verbose_name = u'答案'
        verbose_name_plural = u'答案'

    content = models.TextField(max_length=255, verbose_name=u'答案内容')
    rank = models.IntegerField(default=0, blank=False, verbose_name=u'分数')

    def __unicode__(self):
        return self.content

class Question(models.Model):
    class Meta:
        verbose_name = u'问题'
        verbose_name_plural = u'问题'

    content = models.CharField(max_length=255, verbose_name=u'问题内容')
    anwers = models.ManyToManyField(Answer, verbose_name=u'答案')

    def __unicode__(self):
        return self.content

class Questionnaire(models.Model):
    class Meta:
        verbose_name = u'问卷'
        verbose_name_plural = u'问卷'
        ordering = ['ctime']

    title = models.CharField(max_length=255, verbose_name=u'标题')
    description = models.TextField(verbose_name=u'描述')
    questions = models.ManyToManyField(Question, verbose_name=u'问题集')
    ctime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.title
