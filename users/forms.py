from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Электронная почта", required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth', 'avatar']
        labels = {
            'username': 'Имя пользователя',
            'date_of_birth': 'Дата рождения',
            'avatar': 'Фотография',
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'date_of_birth', 'avatar']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'avatar': 'Фото профиля',
        }