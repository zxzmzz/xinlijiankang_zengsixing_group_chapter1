#coding:utf-8
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import Questionnaire, Answer


@csrf_exempt
def questionnaire(request, id):
    if request.method == 'GET':
        try:
            qn = Questionnaire.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404(u"您访问的问卷不存在")
        return render_to_response('Questionnaire.html', {'qn': qn})

    if request.method == 'POST':
        count = 0
        for aid in request.POST.values():
            count += Answer.objects.get(id=aid).rank
        return HttpResponse('你的得分是{count}'.format(count=count))

def home(request):
    if request.method == 'GET':
        qns=Questionnaire.objects.all()
        if not qns:
            return HttpResponse('目前还没有问卷，请到<a href="/admin/">后台</a>添加')
        else:
            return render_to_response('home.html', {'qns': qns})