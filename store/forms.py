from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from store.models import Feedback
from .models import Order


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_long'}), label='Имя')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input_long'}), label='E-mail')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input_long'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input_long '}), label='Повторите пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInFrom(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_long2'}), label='Имя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input_long2'}), label='Пароль')

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Имя')
    phone = forms.CharField(label='Номер телефона')
    data_birthday = forms.DateField(label='Data birthday')
    phone2 = forms.CharField(label='Номер телефона')
    pin = forms.CharField(label='Введите четыре цифры (Pin)')

    class Meta:
        model = User
        fields = ['email', 'phone', 'data_birthday', 'phone2', 'pin']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {'client_name', 'client_email', 'client_number'}


class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Имя')
    e_mail = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Адрес доставки')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Телефон')


    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'country', 'city', 'street', 'house', 'flat']
