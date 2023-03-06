from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    # password1 = forms.CharField(max_length=50)
    # password2 = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')