from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, logout, login
from . import forms


# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store:home')
    form = forms.SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = forms.SignInFrom(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store:home')
    form = forms.SignInFrom()
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')


def edit_profile(request):
    form = forms.EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('store:home')
    form = forms.EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def reset_password(request):
    form = forms.ChangePasswordForm(request.user, request.POST)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('users:sign_in')
    form = forms.ChangePasswordForm(request.user)
    return render(request, 'reset_password.html', {'form': form})


def profile_detail(request):
    return render(request, 'profile_detail.html')
