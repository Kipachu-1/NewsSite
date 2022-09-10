from multiprocessing import context
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.urls import reverse


def home(request):
    Scince_news = models.ArticleApi.objects.filter(category='Science')[:4]
    Scince_block_large1 = models.ArticleApi.objects.filter(category='Science')[7]
    Scince_block_large = models.ArticleApi.objects.filter(category='Science')[14]
    Scince_block = models.ArticleApi.objects.filter(category='Science')[4:8]
    Tech_block_large = models.ArticleApi.objects.filter(category='Technology')[0] 
    Tech_block = models.ArticleApi.objects.filter(category='Technology')[1:5]
    Board1_Articles = models.ArticleApi.objects.all()
    Space_block_large = models.ArticleApi.objects.filter(category='Space')[7]
    Space_block = models.ArticleApi.objects.filter(category='Space')[4:7]
    Animal_block_large = models.ArticleApi.objects.filter(category='Animal')[0]
    Animal_block = models.ArticleApi.objects.filter(category='Animal')[1:4]
    if request.method == 'POST':
        q = request.POST.get('q') if request.POST.get('q') != None else  ''
        return redirect('search_page', search_data=q)
        
    
    context = {'Board1_Articles': Board1_Articles, 'Scince_news': Scince_news,
               'Scince_block_large': Scince_block_large, 'Scince_block': Scince_block, 'Tech_block_large': Tech_block_large,
               'Tech_block': Tech_block, 'Space_block_large': Space_block_large, 'Space_block': Space_block, 'Scince_block_large1': Scince_block_large1, 
               'Animal_block_large': Animal_block_large, 'Animal_block': Animal_block, 
               }
    
    
    return render(request, 'arsite/home.html', context)



def catogory_page(request, category):
    category_desc = models.Category.objects.get(name=category)
    articles = models.ArticleApi.objects.filter(category=category)
    paginator = Paginator(articles, per_page=20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'category': category, 'category_desc': category_desc.description, 'articles': articles, 'page_obj': page_obj }
    return render(request, 'arsite/category_page.html', context)


def article_page(request, name):
    article_name = str(name).replace('%20', ' ')
    article = models.ArticleApi.objects.get(title=article_name)
    comments = article.comment_set.all().order_by('-created')
    if request.method == 'POST':
        q = request.POST.get('q') 
        if request.POST.get('q') != None:
            return redirect('search_page', search_data=q)
        else:
            pass
    if request.method == 'POST':
        message = models.Comment.objects.create(
            user=request.user.username, article=article, body=request.POST.get('body')
            )  
        return redirect('article_page', article_name)
    context = {
        "article": article, 'comments': comments, 'signbtn': name
    }
    return render(request, 'arsite/article_page.html', context )



def Search_page(request, search_data):
    articles = models.ArticleApi.objects.filter(Q(title__icontains=str(search_data)))
    paginator = Paginator(articles, per_page=20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        q = request.POST.get('q') if request.POST.get('q') != None else  ''
        return redirect('search_page', search_data=q)
    context = {'page_obj': page_obj, 'search_data': str(search_data)}
    return render(request, 'arsite/Search_page.html', context)


def login_page(request, next_page=' '):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            if next_page != ' ':
                return redirect('article_page', name=next_page)
            else:
                return redirect('home')
    context = {
        'next_page': next_page
    }
    print(next_page)   
    return render(request, 'arsite/login_page2.html', context)

def register(request, next_page=' '):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            new_user = User.objects.create_user(username=username, password=password1)
            user = authenticate(request, username=username, password = password1)
            login(request, user)
            if next_page != ' ':
                return redirect('article_page', name=next_page)
            else:
                return redirect('home')
    context = {'next_page': next_page}
    return render(request, 'arsite/SignUp_page.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')


