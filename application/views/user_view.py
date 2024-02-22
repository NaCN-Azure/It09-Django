# views/user_view.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from application.forms.form import CustomUserCreationForm, CustomLoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})