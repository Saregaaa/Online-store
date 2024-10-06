# Generated by Django 4.2.15 on 2024-09-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='carts',
            field=models.ManyToManyField(to='carts.cart', verbose_name='Замовлення'),
        ),
    ]
