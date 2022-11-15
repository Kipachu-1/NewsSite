from django.db import models
from django.contrib.auth.models import User
 





class Authors(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
     
    def __str__(self):
        return self.name
         
   

    
class Article(models.Model):
    Author = models.CharField(max_length=100, unique=False)
    header_image = models.ImageField(upload_to='images/', null=True, blank=True)
    url = models.TextField(unique=True, null=True)
    image_url = models.TextField(null=True)
    category = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=100, null=True)
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(null=True)
    views = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def class_name(self):
        return self.__class__.__name__
    
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    user = models.CharField(max_length=50)
    body = models.TextField()
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)