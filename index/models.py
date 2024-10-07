from django.db import models
from django.db.models import Avg

from users.models import User
# from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'
        ordering = ("id",)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    category = models.ManyToManyField(Categories, related_name='subcategories', verbose_name='Субкатегорії')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'subcategory'
        verbose_name = 'Субкатегорію'
        verbose_name_plural = 'Субкатегорії'
        ordering = ("id",)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Зображення')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Ціна')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Знижка у %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        ordering = ("id",)

    def average_rating(self):
        reviews = self.reviews.all()  # Все отзывы о продукте
        total_reviews = reviews.count()
        
        if total_reviews > 0:
            # Вычисление среднего рейтинга по трём категориям
            total_quality = sum([review.quality_rating for review in reviews])
            total_price = sum([review.price_rating for review in reviews])
            total_value = sum([review.value_rating for review in reviews])
            
            # Средний рейтинг (можно округлить до одного десятичного знака)
            avg_quality = total_quality / total_reviews
            avg_price = total_price / total_reviews
            avg_value = total_value / total_reviews
            
            # Общий средний рейтинг
            avg_rating = (avg_quality + avg_price + avg_value) / 3
            return round(avg_rating, 1)  # Округляем до одного знака после запятой
        return 0  # Если отзывов нет

    def __str__(self):
        return f'{self.name} Кількість - {self.quantity}'

    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price
    

class Reviews(models.Model):
    RATING_CHOICES = [
        (1, '1 зірка'),
        (2, '2 зірки'),
        (3, '3 зірки'),
        (4, '4 зірки'),
        (5, '5 зірок'),
    ]

    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews', verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Користувач')
    name = models.CharField(max_length=80, verbose_name='Ім`я')
    summary = models.CharField('Заголовок', max_length=255)
    review = models.TextField('Відгук', max_length=5000)
    quality_rating = models.IntegerField('Оцінка якості', choices=RATING_CHOICES)
    price_rating = models.IntegerField('Оцінка ціни', choices=RATING_CHOICES)
    value_rating = models.IntegerField('Оцінка цінності', choices=RATING_CHOICES)
    created_at = models.DateTimeField('Дата додання', auto_now_add=True)

    class Meta:
        db_table = 'review'
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.name} - {self.product.name}"