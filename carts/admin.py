from django.contrib import admin

from carts.models import Cart, Order


# admin.site.register(Cart)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'product', 'quantity')

    def get_username(self, obj):
        if obj.user:
            return obj.user.username
        return obj.session_key


admin.site.register(Order)

