from .models import Cart

def cart_context(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
        carts = Cart.objects.filter(session_key=request.session.session_key)

    return {
        'carts': carts,
        'cart_total_price': carts.total_price() if carts.exists() else 0,
        'cart_total_quantity': carts.total_quantity() if carts.exists() else 0,
    }
