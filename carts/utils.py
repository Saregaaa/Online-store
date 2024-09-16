from carts.models import Cart


def get_user_cart(request):
    if request.user.is_authenticated:
        # Если пользователь авторизован, возвращаем корзину по пользователю
        return Cart.objects.filter(user=request.user)
    else:
        # Если нет сессии, создаем новую
        if not request.session.session_key:
            request.session.create()
        # Возвращаем корзину по ключу сессии
        return Cart.objects.filter(session_key=request.session.session_key)

# def get_user_cart(request):
#     if request.user.is_authenticated:
#         return Cart.objects.filter(user=request.user)
    
#     if not request.session.session_key:
#         request.session.create()
#         return Cart.objects.filter(session_key=request.session.session_key)