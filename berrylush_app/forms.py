from django.forms import ModelForm
from . models import Review
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1' ,'password2')
    

        