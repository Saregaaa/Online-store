from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.sign_in, name='login'),
    path('registration', views.sign_up, name='registration'),
    path('logout/', views.logout, name='logout'),
    
]