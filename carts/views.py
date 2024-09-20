from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from carts.forms import OrderForm
from carts.utils import get_user_carts
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST
from carts.models import Cart, Order
from index.models import Products





def cart_add(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)
    
    print(f"Session Key: {request.session.session_key}") # Проверка на сессию

    return redirect(request.META['HTTP_REFERER'])
            
            

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
    carts = get_user_carts(request)  # Получаем корзину
    print(f"Anonymous user, session key: {request.session.session_key}, carts count: {carts.count()}")  # Для отладки

    context = {
        'carts': carts,   
    }
    return render(request, 'carts/user_cart.html', context)

@login_required
def create_order(request):
    # Получаем корзину текущего пользователя
    cart_items = get_user_carts(request)

    if not cart_items.exists():
        return redirect('carts:user_cart')  # Перенаправляем на страницу корзины, если корзина пуста

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Создаем заказ
            order = Order.objects.create(
                user=request.user,
                sity=form.cleaned_data['sity'],
                address=form.cleaned_data['address'],
                postal_code=form.cleaned_data['postal_code']
            )

            # Связываем все элементы корзины с этим заказом
            for item in cart_items:
                order.cart.add(item)  # Сохраняем товары в заказ

            # Очищаем корзину
            cart_items.delete()

            return JsonResponse({'success': True, 'message': 'Ваше замовлення було успішно створено!'})

    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart_items': cart_items,  # Отображение корзины пользователя
    }
    return render(request, 'orders/create_order.html', context)