from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from carts.models import Cart
from users.models import User

from users.forms import UserLoginForm, UserRegistrationForm

# # Create your views here.


def sign_in(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            session_key = request.session.session_key

            # Попробуем найти пользователя по email
            try:
                user = User.objects.get(email=email)
                # Аутентификация по username, так как Django требует username для authenticate
                user = authenticate(username=user.username, password=password)
            except User.DoesNotExist:
                user = None
            
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index:home'))
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = UserLoginForm()

    context = {
        'title': 'Sign In',
        'form': form,
    }
    return render(request, 'users/sign_in.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(reverse('index:home'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Sign Up',
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Ви вийшли з аккаунту")
    auth.logout(request)
    return redirect(reverse('users:login'))
    

#     context = {
#         'title': 'Sign In',
#         'form': form,
#     }
#     return render(request, 'users/sign_in.html', context)

# def sign_in(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             user = auth.authenticate(email=email, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index:home'))
#     else:
#         form = UserLoginForm()
    
#     context = {
#         'title': 'Sign In',
#         'form': form,
#     }
#     return render(request, 'users/sign_in.html', context)