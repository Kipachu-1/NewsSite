from multiprocessing import context
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .NewsApi import runthis
runthis()




def home(request):
    Scince_news = models.Article.objects.filter(category='Science')[:4]
    Scince_block_large1 = models.Article.objects.filter(category='Science')[7]
    Scince_block_large = models.Article.objects.filter(category='Science')[14]
    Scince_block = models.Article.objects.filter(category='Science')[4:8]
    Tech_block_large = models.Article.objects.filter(category='Technology')[0] 
    Tech_block = models.Article.objects.filter(category='Technology')[1:5]
    Board1_Articles = models.Article.objects.all()
    Space_block_large = models.Article.objects.filter(category='Space')[0]
    Space_block = models.Article.objects.filter(category='Space')[1:4]
    Animal_block_large = models.Article.objects.filter(category='Science')[10]
    Animal_block = models.Article.objects.filter(category='Science')[17:20]
    Health_block_large =  models.Article.objects.filter(category='Health')[0]
    Health_block =  models.Article.objects.filter(category='Health')[1:4]
    Life_hack_large = models.Article.objects.filter(category='Science')[5]
    Life_hack_block = models.Article.objects.filter(category='Science')[8:11]

    if request.method == 'POST':
        q = request.POST.get('q') if request.POST.get('q') != None else  ''
        return redirect('search_page', search_data=q)
        
    
    context = {'Board1_Articles': Board1_Articles, 'Scince_news': Scince_news,
               'Scince_block_large': Scince_block_large, 'Scince_block': Scince_block, 'Tech_block_large': Tech_block_large,
               'Tech_block': Tech_block, 'Space_block_large': Space_block_large, 'Space_block': Space_block, 'Scince_block_large1': Scince_block_large1, 
               'Animal_block_large': Animal_block_large, 'Animal_block': Animal_block, 'Health_block': Health_block, "Health_block_large" : Health_block_large,
               'Life_hack_block': Life_hack_block, "Life_hack_large": Life_hack_large
               }
    
    
    return render(request, 'arsite/home.html', context)



def catogory_page(request, category):
    if request.method == 'POST':
        q = request.POST.get('q') 
        if request.POST.get('q') != None:
            return redirect('search_page', search_data=q)
        else:
            pass
    try:
        if category == 'Latest':
            category_desc = 'you are reading latest news from the world'
            articles = models.Article.objects.all().order_by('-created')
        elif category == 'Authors':
            category_desc = 'you are reading articles of Authors'
            articles = models.Article.objects.all().order_by('-created')
        else:
            category_desc = models.Category.objects.get(name=category).description
            articles = models.Article.objects.filter(Q(category__icontains=str(category))).order_by('-created')
    except:
        category_desc = 'you are reading artilces with this category'
        articles = models.Article.objects.filter(Q(category__icontains=str(category))).order_by('-created')
    paginator = Paginator(articles, per_page=20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'category': category, 'category_desc': category_desc, 'articles': articles, 'page_obj': page_obj }
    return render(request, 'arsite/category_page.html', context)


def article_page(request, name):
    article_name = str(name).replace('%20', ' ')
    if request.method == 'POST':
        q = request.POST.get('q') 
        if request.POST.get('q') != None:
            return redirect('search_page', search_data=q)
        else:
            pass
    try:
        article = models.Article.objects.get(title=article_name)
        comments = article.comment_set.all().order_by('-created')
        article.views += 1
        article.save()
        if request.method == 'POST':
            message = models.Comment.objects.create(
                user=request.user.username, article=article, body=request.POST.get('body')
                )  
            return redirect('article_page', article_name)
    except:
        article = models.Article.objects.get(title=article_name)
        comments = article.comment_written_set.all().order_by('-created')
        article.views += 1
        article.save()
        if request.method == 'POST':
            message = models.Comment_written.objects.create(
                user=request.user.username, article=article, body=request.POST.get('body')
                )  
            return redirect('article_page', article_name)
    context = {
        "article": article, 'comments': comments, 'signbtn': name, 'categories': article.category.split(',')
    }
    return render(request, 'arsite/article_page.html', context )



def Search_page(request, search_data):
    articles = models.Article.objects.filter(Q(title__icontains=str(search_data)))
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
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password!')
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

@login_required(login_url='login/')
def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('Title')
        subtitle = request.POST.get('Subtitle')
        category = request.POST.get('categories')
        header_image = request.FILES['header_image']
        body = request.POST.get('Body')
        try:
            models.Article.objects.create(Author=request.user.username, title=title, subtitle = subtitle, 
                                      header_image=header_image, body=body, category=category)
            return redirect('studio', section=' ')
        except:
            return redirect('studio', section=' ')
    return render(request, 'arsite/edit_article.html')

@login_required(login_url='login/')
def change_article(request, name):
    article = models.Article.objects.get(title=name)
    if request.user.username != article.Author:
        return redirect('home')
    context = {'article': article}
    if request.method == 'POST':
        article.title = request.POST.get('Title')
        article.subtitle = request.POST.get('Subtitle')
        article.category = request.POST.get('categories')
        try:
            article.header_image = request.FILES['header_image']
        except: 
            pass
        article.body = request.POST.get('Body')
        article.save()
        return redirect('studio', section=' ')
        
    return render(request, 'arsite/edit_article.html', context)

def delete_article(request, name):
    article_delete = models.Article.objects.get(title=name)
    if request.user.username != article_delete.Author:
        return redirect('home')
    if request.method == 'POST':
        article_delete.delete()
    context = {
        'title': name
    }
        
    return render(request, 'arsite/delete.html', context)
    

@login_required(login_url='login/')
def Author_studio(request, section): 
    list_articles = models.Article.objects.filter(Author=request.user.username)
    views = 0
    for i in list_articles:
        views += i.views
    last_list_articles = list_articles[:5]
    comments = models.Comment.objects.filter(article__Author__contains=str(request.user.username)).order_by('-created')
    
    context = {
        'list_articles':list_articles,
        'views': views,
        'last_list_articles': last_list_articles,
        'comments' : comments
    }
    if section == 'articles':
        return render(request, 'arsite/Studio_articles.html', context)
    elif section == 'commentaries':
        return render(request, 'arsite/Studio_commentaries.html', context)
    elif section == 'statistics':
        return render(request, 'arsite/Studio_statistics.html', context)
    return render(request, 'arsite/Studio.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')



