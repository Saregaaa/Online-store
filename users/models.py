from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефону')
    avatar = models.ImageField(upload_to='user/', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username
