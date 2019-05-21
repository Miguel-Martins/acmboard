from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.urls import reverse_lazy
from board.forms import UserForm
from users.models import Profile
from django.contrib.auth.models import User
from bootstrap_modal_forms.generic import BSModalUpdateView

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


class UserUpdateView(BSModalUpdateView):
    model = User
    template_name = 'users/update-user.html'
    form_class = UserForm
    success_url = reverse_lazy('home')

class UserProfileUpdateView(BSModalUpdateView):
    model = Profile
    template_name = 'users/update-profile.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('home')

