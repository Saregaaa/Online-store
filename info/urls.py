from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('faq/', views.faq, name='faq'),
   
]
