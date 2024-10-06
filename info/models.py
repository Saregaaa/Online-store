from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=80, verbose_name='Ім`я')
    email = models.EmailField(max_length=254, verbose_name='Email')
    title = models.TextField(max_length=200, verbose_name='Заголовок')
    comment = models.TextField(max_length=5000, verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    class Meta:
        db_table = 'contact'
        ordering = ['created_at']
        verbose_name = 'Новий коментар'
        verbose_name_plural = 'Нові коментарі'


    def __str__(self):
        return f"{self.name } - {self.title}"
    

class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name='Питання')
    answer = models.TextField(max_length=5000, verbose_name='Відповідь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    class Meta:
        db_table = 'faq'
        ordering = ['created_at']
        verbose_name = 'Часті запитання'
        verbose_name_plural = 'Часті запитання'

    def __str__(self):
        return self.question