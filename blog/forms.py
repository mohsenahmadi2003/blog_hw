from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken.')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already registered.')

        # Check if both password fields match
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Email / Username", max_length=254)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
