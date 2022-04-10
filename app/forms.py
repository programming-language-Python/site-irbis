from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Имя пользователя', 'minlength': 5}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'id': 'pass', 'placeholder': 'Пароль', 'minlength': 6}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Имя пользователя', 'minlength': 5}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'id': 'pass', 'placeholder': 'Пароль', 'minlength': 6}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'id': 'passConfirm', 'placeholder': 'Потвердите пароль', 'minlength': 6}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
