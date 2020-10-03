from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.Form):
    email=forms.EmailField()
    bio = forms.CharField(max_length=1000, required=False)
    nickname = forms.CharField(max_length=250, required=False)
    '''class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'nickname']'''

'''class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']'''