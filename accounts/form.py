from dataclasses import fields
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']



class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = ['city','phone_number','image']