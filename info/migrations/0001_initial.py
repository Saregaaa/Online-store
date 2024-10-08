# Generated by Django 4.2.15 on 2024-09-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Ім`я')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('title', models.TextField(max_length=200, verbose_name='Заголовок')),
                ('comment', models.TextField(max_length=5000, verbose_name='Коментар')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
            ],
            options={
                'verbose_name': 'Новий коментар',
                'verbose_name_plural': 'Нові коментарі',
                'db_table': 'contact',
                'ordering': ['created_at'],
            },
        ),
    ]
