from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

def login(request):
    return render(request, 'users/login.html', {'title':'Login'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title':'Register'})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            return redirect('register')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form, 'title':'Login'})

