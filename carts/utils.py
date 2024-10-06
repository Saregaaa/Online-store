from carts.models import Cart


# def get_user_carts(request):
#     if request.user.is_authenticated:
#         return Cart.objects.filter(user=request.user)
    
#     if not request.session.session_key:
#         request.session.create()
#     return Cart.objects.filter(session_key=request.session.session_key)

# def get_user_carts(request):
#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user)
#         print(f"Authenticated user, carts count: {carts.count()}")
#         return carts
    
#     if not request.session.session_key:
#         request.session.create()

#     carts = Cart.objects.filter(session_key=request.session.session_key)
#     print(f"Anonymous user, session key: {request.session.session_key}, carts count: {carts.count()}")
#     return carts

import logging

logger = logging.getLogger(__name__)
def get_user_carts(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
    else:
        # Создаем session_key, если он отсутствует
        if not request.session.session_key:
            request.session.create()

        # Убедись, что session_key корректен
        session_key = request.session.session_key
        print(f"Session Key: {session_key}")  # Для отладки
        
        # Получаем корзину по session_key
        carts = Cart.objects.filter(session_key=session_key)

        logger.info(f"User {request.user.username if request.user.is_authenticated else 'Anonymous'}, "
                f"session key: {request.session.session_key}, carts count: {carts.count()}")


    return carts

