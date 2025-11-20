from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomRegisterForms


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, "Login yoki parol xato!")
            return redirect('login_page')
    return render(request, template_name='users/login.html')

def register_page(request):
    if request.method == 'POST':
        form = CustomRegisterForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # avtomatik login
            messages.success(request, "Muvaffaqiyatli ro‘yxatdan o‘tdingiz!")
            return redirect('profile')
        else:
            messages.error(request, "Ma'lumotlarda xatolik bor. Tekshirib qayta urinib ko‘ring.")

    else:
        form = CustomRegisterForms()
    return render(request, 'users/register.html', {'form': form})

@login_required
def logout_page(request):
    logout(request)
    return redirect('home_page')
