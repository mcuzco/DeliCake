from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    class Meta ():
        model = User
        fields = ['username','first_name', 'last_name' ,'email','password1', 'password2']
        help_texts = {k:"" for k in fields}

class loginForm (AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password', }))
    remember_me = forms.BooleanField(required=False)