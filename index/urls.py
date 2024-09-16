from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('search/', views.shop, name='search'),
    path('shop/<slug:subcategory_slug>/', views.shop, name='shop_subcategory'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
]