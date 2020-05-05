from django import forms
from .models import Team

class VoteForm(forms.Form):
    vote_choice = (
        (1, '')
    )

    username = forms.CharField(label='username', max_length=32,
                               widget=forms.TextInput(
                                   attrs={'class': 'validate', 'placeholder': 'Username', 'required': "true"}))
    password = forms.CharField(label='password', max_length=64,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password', 'required': "true"}))