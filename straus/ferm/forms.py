from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Client, Product, Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), help_text='Имя пользователя должно состоять максимум из 64 символов')
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), help_text='Имя пользователя должно состоять максимум из 64 символов')
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-mail',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=64,label='Фамилия',widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=64,label='Имя',widget=forms.TextInput(attrs={'class': 'form-control'}))
    # patronymic = forms.CharField(max_length=64,label='Отчество',widget=forms.TextInput(attrs={'class': 'form-control'}))
    # PassportSeries = forms.IntegerField(label='Серия паспорта')
    # PassportID = forms.IntegerField(label='Номер паспорта')
    # PhoneNumber = forms.IntegerField(label='Номер телефона')


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            # 'patronymic',
            # 'PassportSeries',
            # 'PassportID',
            # 'PhoneNumber',
            'password1',
            'password2'
        )

class OrderForm(forms.Form):
    Count = forms.IntegerField(label='Количество: ')

