import time
import requests
from . import models

current_time = time.strftime("%Y-%m-%d")
url_science = ('https://newsapi.org/v2/everything?'
       'q=science&'
       'domains=sciencenews.org,livescience.com,popsci.com&'
       f'from={current_time}&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')

url_live = ('https://newsapi.org/v2/everything?'
       'domains=livescience.com&'
       f'from={current_time}&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')

url_space = ('https://newsapi.org/v2/everything?'
       'q=space&'
       'domains=sciencenews.org,livescience.com&'
      f'from={current_time}&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')

url_tech = ('https://newsapi.org/v2/everything?'
       'q=technology&'
       'domains=sciencenews.org,livescience.com&'
       f'from={current_time}&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_animal = ('https://newsapi.org/v2/everything?'
       'q=animal&'
       'domains=sciencenews.org,livescience.com,popsci.com&'
       f'from={current_time}&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_geor = ('https://newsapi.org/v2/everything?'
       'q=geography&'
       'domains=sciencenews.org,livescience.com,popsci.com&'
       f'from={current_time}&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')

url_heal = ('https://newsapi.org/v2/everything?'
       'q=health&'
       f'from={current_time}&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')

def runthis():
       if str(current_time) not in str(models.Article.objects.last().created):
              top_headlines_science = requests.get(url_science).json()
              for article in top_headlines_science['articles']:
                     try:       
                            models.Article.objects.create(
                            Author=article['author'], category='Science',
                            image_url=article['urlToImage'], title=article['title'], 
                            url=article['url']
                            )
                     except: 
                            pass            
              top_headlines_science = requests.get(url_live).json()
              for article in top_headlines_science['articles']:
                     try:
                            models.Article.objects.create(
                            Author=article['author'], category='Science',
                            image_url=article['urlToImage'], title=article['title'], 
                            url=article['url']
                            )
                     except: 
                            pass
                            
              top_headlines_tech = requests.get(url_tech).json()
              for article in top_headlines_tech['articles']:
                     try:
                            
                            models.Article.objects.create(
                            Author=article['author'], category='Technology',
                            image_url=article['urlToImage'], title=article['title'], 
                            url=article['url']
                            )
                            
                     except: 
                            pass


              top_headlines_space = requests.get(url_space).json()
              for article in top_headlines_space['articles']:
                     try:

                            models.Article.objects.create(
                            Author=article['author'], category='Space',
                            image_url=article['urlToImage'], title=article['title'], 
                            url=article['url']
                            )
                     except: 
                            pass


              top_headlines_animal = requests.get(url_animal).json()
              for article in top_headlines_animal['articles']:
                     try:
                            models.Article.objects.create(
                                          Author=article['author'], category='Animal',
                                          image_url=article['urlToImage'], title=article['title'], 
                                          url=article['url']
                                          )
                     except: 
                            pass
              top_headlines_geor = requests.get(url_geor).json()
              for article in top_headlines_geor['articles']:
                     try:
                            models.Article.objects.create(
                                          Author=article['author'], category='Geography',
                                          image_url=article['urlToImage'], title=article['title'], 
                                          url=article['url']
                                          )
                     except: 
                            pass
              top_headlines_health = requests.get(url_heal).json()
              for article in top_headlines_health['articles'][:10]:
                     try:
                            models.Article.objects.create(
                                          Author=article['author'], category='Health',
                                          image_url=article['urlToImage'], title=article['title'], 
                                          url=article['url']
                                          )
                     except: 
                            pass
                     
              print('done')   
              
               
def runthis2():                 
       bad = ['Coombes', 'http']
       for i in models.Article.objects.all():
              for word in bad:
                     if word in i.Author:
                            i.delete()
              if '@' in i.Author:
                     i.Author = 'Frank Kauper'
                     i.save()
              
                            
       from bs4 import BeautifulSoup
       for article in models.Article.objects.filter(body=None):     
              response = requests.get(article.url)
              soup = BeautifulSoup(response.text, 'lxml')
              text = ''
              tags = soup.find_all(['h3', 'p'])
              for tag in tags:
                     text += f"{tag.text}\n"    
                     
              text += 'Thumbs up to see more articles about interesting things in your feed!'
              article.body = text
              article.save()

