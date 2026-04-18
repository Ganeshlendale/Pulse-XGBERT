from django.shortcuts import render

# Create your views here.

####################################
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    UserRegisterForm, UserLoginForm,
    UserUpdateForm, ProfileUpdateForm,
    CustomPasswordChangeForm
)
from .models import Profile


def register_view(request):
    if request.user.is_authenticated:
        return redirect('pages:dashboard')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.first_name}!')
            return redirect('pages:dashboard')
    else:
        form = UserRegisterForm()

    return render(request, 'profile_system/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('pages:dashboard')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            next_url = request.GET.get('next', 'pages:dashboard')
            return redirect(next_url)
    else:
        form = UserLoginForm()

    return render(request, 'profile_system/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('core:landing')


@login_required
def profile_detail_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile_system/profile_detail.html', {'profile': profile})


@login_required
def profile_edit_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile_system:profile_detail')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile_system/profile_edit.html', context)


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully!')
            return redirect('profile_system:profile_detail')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'profile_system/change_password.html', {'form': form})


@login_required
def delete_account_view(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('profile_system:register')

    return render(request, 'profile_system/delete_account.html')
