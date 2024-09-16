from django import template

from carts.models import Cart


register = template.Library()


@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    

@register.filter
def multiply(value, arg):
    try:
        return round(float(value) * float(arg), 2)
    except (ValueError, TypeError):
        return 0