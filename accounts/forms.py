from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('confirm_password')
        if p1 and p2:
            if p1 != p2:
                raise ValidationError("password and confirm password not math")
        return cleaned_data

class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

