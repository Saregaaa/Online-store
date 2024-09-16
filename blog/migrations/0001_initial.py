# Generated by Django 4.2.15 on 2024-09-16 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Новий пост',
                'verbose_name_plural': 'Нові пости',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Ім`я')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('title', models.TextField(max_length=200, verbose_name='Заголовок')),
                ('comment', models.TextField(max_length=5000, verbose_name='Коментар')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Новий коментар',
                'verbose_name_plural': 'Нові коментарі',
                'db_table': 'blog_comment',
                'ordering': ['created_at'],
            },
        ),
    ]
