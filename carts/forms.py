from django import forms
from .models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['city', 'address', 'postal_code']  # Поля, которые будут запрашиваться у пользователя
        labels = {
            'city': 'Місто',
            'address': 'Адреса',
            'postal_code': 'Поштовий індекс',
        }
