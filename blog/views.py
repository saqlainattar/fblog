from django.shortcuts import render
from.models import Article
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    # return HttpResponse('welcome on homepage')
    return render(request,'blog/homepage.html')

def article_list(request):
    # return render(request,'blog/article_list.html')

    articles = Article.objects.all().order_by('date')
    return render(request,'blog/article_list.html',{'articles':articles})

def article_detail(request,id):
    article = Article.objects.get(id=id)
    return render(request,'blog/article_detail.html',{'article':article})