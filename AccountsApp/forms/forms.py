from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormUser(UserCreationForm):
    username = forms.CharField(label="Username", required=True, max_length=25,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input100'}))
    first_name = forms.CharField(label="First_name", required=True, max_length=25,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label="Last_name", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label="Email", required=True, max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirm',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k: "" for k in fields}
