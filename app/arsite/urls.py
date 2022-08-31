from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>', views.catogory_page, name='category_page'),
    path("article/<str:name>", views.article_page, name="article_page")
]

