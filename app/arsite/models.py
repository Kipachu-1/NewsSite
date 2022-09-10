from django.db import models
from django.contrib.auth.models import User
 





class Authors(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
     
    def __str__(self):
        return self.name
         
   
class ArticleApi(models.Model):
    Author = models.CharField(max_length=50, unique=False)
    url = models.TextField(unique=True)
    header_image = models.TextField()
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Article(models.Model):
    Author = models.ForeignKey(Authors, on_delete=models.PROTECT)
    header_image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    article = models.ForeignKey(ArticleApi, on_delete=models.CASCADE)
    user = models.TextField(max_length=20, null=True)
    body = models.TextField()


    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    