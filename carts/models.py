from django.db import models

from index.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:   
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Користувач")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Кількість')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата оновлення')

    class Meta:
        db_table = 'carts'
        verbose_name = 'Корзину'
        verbose_name_plural = 'Корзини'

    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
        

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username} with {self.product.name}"
        return f"Cart for session {self.session_key} with {self.product.name}"


class Order(models.Model):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="Користувач")
    carts = models.ManyToManyField(Cart, verbose_name="Замовлення")
    city = models.CharField(max_length=50, verbose_name="Місто")
    address = models.CharField(max_length=150, verbose_name="Адреса") 
    postal_code = models.CharField(max_length=10, verbose_name="Поштовий індекс")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        db_table = 'order'
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f"Замовлення {self.user.username} | №{self.id} | Дата створення: {self.create_at}"
    