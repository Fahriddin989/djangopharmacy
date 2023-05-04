from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':
                                                                 'Имя пользователя',
                                                             'class': 'w-full py-4 px-6 rounded xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':
                                                                      'Пароль',
                                                                  'class': 'w-full py-4 px-6 rounded xl'}))



class SignupForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email','phone',  'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':
                                                                 'Your username',
                                                             'class': 'w-full py-4 px-6 rounded xl'}))

    phone = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':
                                                               '+998901234567',
                                                           'class': 'w-full py-4 px-6 rounded xl'}))

    mail = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':
                                                              'Your email',
                                                          'class': 'w-full py-4 px-6 rounded xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':
                                                                      'Your password',
                                                                  'class': 'w-full py-4 px-6 rounded xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':
                                                                      'Repeat password',
                                                                  'class': 'w-full py-4 px-6 rounded xl'}))
