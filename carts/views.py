from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from carts.utils import get_user_cart


from carts.models import Cart
from index.models import Products



def cart_add(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)

    if request.user.is_authenticated:
        # Корзина для авторизованных пользователей
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        cart.quantity += 1
        cart.save()
    else:
        # Корзина для анонимных пользователей
        if not request.session.session_key:
            request.session.create()  # Создаем новую сессию, если ее нет

        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key, product=product)
        cart.quantity += 1
        cart.save()

    return redirect(request.META.get('HTTP_REFERER', 'index:home'))

# def cart_add(request, product_slug):
    
#     product = Products.objects.get(slug=product_slug)

#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, product=product)

#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(user=request.user, product=product, quantity=1)

#     else:
#         carts = Cart.objects.filter(
#             session_key=request.session.session_key, product=product)

#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(
#                 session_key=request.session.session_key, product=product, quantity=1)

#     return redirect(request.META['HTTP_REFERER'])
            
            

def cart_change(request, product_slug):
    ...

def cart_remove(request, cart_id):


    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])


def cart_update_quantity(request, cart_id, action):
    # Получаем объект корзины по ID
    cart = get_object_or_404(Cart, id=cart_id)

    if action == 'plus':
        cart.quantity += 1  # Увеличиваем количество на 1
    elif action == 'minus' and cart.quantity > 1:
        cart.quantity -= 1  # Уменьшаем количество на 1, но не ниже 1

    cart.save()  # Сохраняем изменения
    return redirect(request.META.get('HTTP_REFERER', 'index:home'))
   

def users_cart(request):
    carts = get_user_cart(request)  # Получаем корзину
    

    context = {
        'carts': carts,   
    }
    return render(request, 'carts/user_cart.html', context)