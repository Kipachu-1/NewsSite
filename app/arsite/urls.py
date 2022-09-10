from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>', views.catogory_page, name='category_page'),
    path('article/<str:name>', views.article_page, name="article_page"),
    path('search/<str:search_data>', views.Search_page, name='search_page' ),
    path("login/<str:next_page>",views.login_page, name='login_page'),
    path("register/<str:next_page>", views.register, name='signup_page'),
    path('logout', views.logout_user, name='logout_page'),
    path("login/",views.login_page, name='login_page_default'),
    path("register/", views.register, name='signup_page_default'),
    
]


