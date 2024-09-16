from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from index.models import Categories, Products, Reviews, Subcategory
from index.utils import q_search


# Create your views here.
def home(request):
    return render(request, 'home.html')

def shop(request, subcategory_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    # Если слаг подкатегории передан, пытаемся получить подкатегорию
    subcategory = None
    if subcategory_slug:
        try:
            subcategory = Subcategory.objects.get(slug=subcategory_slug)
        except Subcategory.DoesNotExist:
            subcategory = None

    # Загружаем все категории с предзагрузкой подкатегорий
    categories = Categories.objects.prefetch_related('subcategories').all()

    # Если есть поисковый запрос, используем q_search
    if query:
        products = q_search(query)
    elif subcategory:
        # Если выбрана подкатегория, фильтруем продукты по ней
        products = Products.objects.filter(subcategory=subcategory)
    else:
        # Если подкатегория не выбрана, показываем все продукты
        products = Products.objects.all()

    # Фильтрация по скидке
    if on_sale:
        products = products.filter(discount__gt=0)

    # Сортировка товаров
    if order_by and order_by != "default":
        products = products.order_by(order_by) 

    paginator = Paginator(products, 6)
    current_page = paginator.page(int(page))

    context = {
        'categories': categories,
        'products': current_page,
        'subcategory': subcategory,
        'slug_url': subcategory_slug,
        'on_sale': on_sale,
        'order_by': order_by,
        'query': query
        
    }
    return render(request, 'shop.html', context)

# def shop(request, subcategory_slug):
#     subcategory = Subcategory.objects.filter(subcategory__slug=subcategory_slug)

#     categories = Categories.objects.prefetch_related('subcategories').all()  # Предзагрузка подкатегорий вместе с категориями
    
#     products = Products.objects.all()
    
#     context = {
#         'categories': categories,
#         'products': products,
#         'subcategory': subcategory
#     }
#     return render(request, 'shop.html', context)

def product_detail(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    related_products = Products.objects.filter(subcategory=product.subcategory).exclude(id=product.id)[:6]
    reviews = Reviews.objects.filter(product=product)

    if request.method == 'POST':
        quality_rating = request.POST.get('quality_rating')
        price_rating = request.POST.get('price_rating')
        value_rating = request.POST.get('value_rating')
        name = request.POST.get('name')
        summary = request.POST.get('summary')
        review = request.POST.get('review')


# Проверяем, что рейтинги не пустые
        if not (quality_rating and price_rating and value_rating):
            # Если один из рейтингов пустой, можно отдать сообщение об ошибке
            return render(request, 'product_detail.html', {
                'product': product,
                'related_products': related_products,
                'error_message': 'Пожалуйста, заполните все оценки.'
            })
        
        try:
            # Убедимся, что оценки — это числа и не None
            quality_rating = int(quality_rating) if quality_rating else None
            price_rating = int(price_rating) if price_rating else None
            value_rating = int(value_rating) if value_rating else None

            # Сохраняем отзыв в базу данных
            Reviews.objects.create(
                product=product,
                name=name,
                summary=summary,
                review=review,
                quality_rating=int(quality_rating),
                price_rating=int(price_rating),
                value_rating=int(value_rating)
            )
            return redirect('index:product_detail', product_slug=product.slug)
        
        except (IntegrityError, ValueError) as e:
            # Если возникла ошибка при сохранении или преобразовании в int
            return render(request, 'product_detail.html', {
                'product': product,
                'related_products': related_products,
                'error_message': f'Произошла ошибка: {e}. Попробуйте еще раз.'
            })

        
        
    # Обработка формы
    # if request.method == "POST":
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         review = form.save(commit=False)
    #         review.product = product
    #         review.save()
    #         return redirect('index:product_detail', product_slug=product.slug)
    # else:
    #     form = ReviewForm()
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
        # 'form': form
    }
    return render(request, 'product_detail.html', context)