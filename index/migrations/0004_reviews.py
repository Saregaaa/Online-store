# Generated by Django 4.2.15 on 2024-09-15 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('summary', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('review', models.TextField(max_length=5000, verbose_name='Відгук')),
                ('quality_rating', models.IntegerField(choices=[(1, '1 зірка'), (2, '2 зірки'), (3, '3 зірки'), (4, '4 зірки'), (5, '5 зірок')], verbose_name='Оцінка якості')),
                ('price_rating', models.IntegerField(choices=[(1, '1 зірка'), (2, '2 зірки'), (3, '3 зірки'), (4, '4 зірки'), (5, '5 зірок')], verbose_name='Оцінка ціни')),
                ('value_rating', models.IntegerField(choices=[(1, '1 зірка'), (2, '2 зірки'), (3, '3 зірки'), (4, '4 зірки'), (5, '5 зірок')], verbose_name='Оцінка цінності')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата додання')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='index.products', verbose_name='Продукт')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
                'db_table': 'review',
                'ordering': ['created_at'],
            },
        ),
    ]
