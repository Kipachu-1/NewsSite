from newsapi import NewsApiClient
import requests

url_environment = ('https://newsapi.org/v2/everything?'
       'q=environment&'
       'from=2022-08-31&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_science = ('https://newsapi.org/v2/everything?'
       'q=science&'
       'from=2022-08-31&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_space = ('https://newsapi.org/v2/everything?'
       'q=space&'
       'from=2022-08-31&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_health = ('https://newsapi.org/v2/everything?'
       'q=health&'
       'from=2022-08-31&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_tech = ('https://newsapi.org/v2/everything?'
       'q=technology&'
       'from=2022-08-31&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_animal = ('https://newsapi.org/v2/everything?'
       'q=animal&'
       'from=2022-08-31&'
       'sortBy=relevancy&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')
url_life_hack = ('https://newsapi.org/v2/everything?'
       'q=life-hack&'
       'from=2022-08-31&'
       'sortBy=popularity&'
       'apiKey=e6d26319f3834e4ea9573362bdc740e9')

top_headlines_science = requests.get(url_science).json()

top_headlines_tech = requests.get(url_tech).json()

top_headlines_space = requests.get(url_space).json()


top_headlines_health = requests.get(url_health).json()

top_headlines_environ = requests.get(url_environment).json()

top_headlines_animal = requests.get(url_animal).json()

top_headlines_lifehack = requests.get(url_life_hack).json()





    