# Generated by Django 4.2.15 on 2024-09-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Ім`я'),
        ),
    ]
