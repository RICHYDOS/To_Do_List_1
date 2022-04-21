from django import forms
from django.forms import ModelForm, widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

CustomerFormSet = inlineformset_factory(
        Customer, Item, fields=['item'], extra=1, can_delete=False,
        widgets= {
            'item': forms.TextInput(attrs={'placeholder': 'Enter a task here'}),
        }
        )

