
from . import models
from django.shortcuts import render
from . import NewsApi


def home(request):
    Scince_news = NewsApi.top_headlines_science['articles'][:4]
    Scince_block_large1 = NewsApi.top_headlines_science['articles'][9]
    Scince_block_large = NewsApi.top_headlines_science['articles'][4]
    Scince_block = NewsApi.top_headlines_science['articles'][5:8]
    Tech_block_large =  NewsApi.top_headlines_science['articles'][5]
    Tech_block = NewsApi.top_headlines_science['articles'][:3]
    Board1_Articles = models.Article.objects.all()[:4]
    Space_block_large = NewsApi.top_headlines_space['articles'][0]
    Space_block = NewsApi.top_headlines_space['articles'][1:4]
    Health_block_large = NewsApi.top_headlines_health['articles'][0]
    Health_block = NewsApi.top_headlines_health['articles'][1:4]
    Animal_block_large = NewsApi.top_headlines_animal['articles'][0]
    Animal_block = NewsApi.top_headlines_animal['articles'][1:4]
    Life_hack_large = NewsApi.top_headlines_lifehack['articles'][0]
    Life_hack_block = NewsApi.top_headlines_lifehack['articles'][1:4]
     
    context = {'Board1_Articles': Board1_Articles, 'Scince_news': Scince_news,
               'Scince_block_large': Scince_block_large, 'Scince_block': Scince_block, 'Tech_block_large': Tech_block_large,
               'Tech_block': Tech_block, 'Space_block_large': Space_block_large, 'Space_block': Space_block, 'Scince_block_large1': Scince_block_large1,
               'Health_block_large': Health_block_large, 'Health_block': Health_block, 
               'Animal_block_large': Animal_block_large, 'Animal_block': Animal_block, 
               'Life_hack_large': Life_hack_large, 'Life_hack_block': Life_hack_block}
    
    
    return render(request, 'arsite/home.html', context)



def catogory_page(request, category):
    category_desc = models.Category.objects.get(name=category)
    if category == 'Science':
        articles = NewsApi.top_headlines_science['articles']
    elif category == 'Environment':
        articles = NewsApi.top_headlines_environ['articles']
    elif category == 'Technology':
        articles = NewsApi.top_headlines_tech['articles']
        
    context = {'category': category, 'category_desc': category_desc.description, 'articles': articles }
    return render(request, 'arsite/category_page.html', context)


def article_page(request, name):
    article = models.Article.objects.get(name=name)
    context = {
        "article": article
    }
    return render(request, 'arsite/article_page.html', context )