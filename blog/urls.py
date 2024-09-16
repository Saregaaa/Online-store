from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('search/', views.blog, name='search'),
    path('', views.blog, name='blog'),
    path('blog_details/<slug:slug>/', views.blog_details, name='blog_details'),
]
