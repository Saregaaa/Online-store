from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>', views.cart_add, name='cart_add'),
    path('cart_change/<slug:product_slug>', views.cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>', views.cart_remove, name='cart_remove'),
    path('user_cart', views.users_cart, name='user_cart'),
    path('cart_update_quantity/<int:cart_id>/<str:action>/', views.cart_update_quantity, name='cart_update_quantity'),
    
]