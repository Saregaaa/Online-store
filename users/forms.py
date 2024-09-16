from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'username', 
            'phone', 
            'password1', 
            'password2',
        )

    email = forms.CharField()
    username = forms.CharField()
    phone = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

# class UserLoginForm(AuthenticationForm):
#     email = forms.CharField()
#     password = forms.CharField()

#     class Meta:
#         model = User