from django.urls import path

from .views import blog_list, create_blog, blog_detail, blog_update, news_list, like_post, news_post

urlpatterns=[
    path('',blog_list,name='blog_list'),
    path('news/',news_list,name='news_list'),
    path('news/<int:pk>/',news_post,name='news_detail'),
    path('news/likes/',like_post,name='like_post'),
    path('create/',create_blog,name='blog_create'),
    path('blog/<int:pk>/',blog_detail,name='blog_detail'),
    path('blog-update/<int:pk>/',blog_update,name='blog_update'),
]