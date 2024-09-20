from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['sity', 'address', 'postal_code']  # Поля, которые будут запрашиваться у пользователя
        labels = {
            'sity': 'Місто',
            'address': 'Адреса',
            'postal_code': 'Поштовий індекс',
        }
