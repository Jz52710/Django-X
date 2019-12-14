from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from .models import Question
# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-pub_date').all()
    return render(request,'poll/index.html',{'question_list':question_list})

def detail(request,id):
    question = get_object_or_404(Question, pk=id)
    if request.method == "GET":
        return render(request,'poll/detail.html',{'question':question})
    elif request.method == "POST":
        cid = request.POST.get('id')
        choice = question.choice_set.filter(id=cid)[0]
        choice.votes+=1
        choice.save()
        return redirect('polls:show',id=choice.id)

def show(request,id):
    question = get_object_or_404(Question, pk=id)
    return render(request,"poll/show.html",{'question':question})
