from django import forms
from .models import CartItem, SIZE_CHOICES, THICKNESS_CHOICES
from store.models import Feedback, Order


class RateForm(forms.ModelForm):
    size = forms.ChoiceField(choices=SIZE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio_select '}), )
    thickness = forms.ChoiceField(choices=THICKNESS_CHOICES,
                                  widget=forms.RadioSelect(attrs={'class': 'radio_selects'}), )

    class Meta:
        model = CartItem
        fields = ('size', 'thickness')


class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {'client_name', 'client_email', 'client_number'}


class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Имя')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Адрес доставки')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Телефон')

    class Meta:
        model = Order
        fields = ['name', 'address', 'phone']
