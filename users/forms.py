from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Write your username')
    email = forms.EmailField(label='Write your email')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInFrom(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(BulmaMixin, forms.ModelForm):
    username = forms.CharField(label='Write your username')
    first_name = forms.CharField(label='Write your first name')
    number = forms.IntegerField(label='Write your number')
    birthdate = forms.DateTimeField(label='Write your birthdate')
    last_name = forms.CharField(label='Write your last name')
    email = forms.EmailField(label='Write your email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangePasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
