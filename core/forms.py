
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from booking.models import Booking


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'w-full py-2 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'w-full py-2 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', ]

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'w-full py-2 rounded-xl'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'w-full py-2 rounded-xl'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'w-full py-2 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'your email address',
        'class': 'w-full py-2 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'w-full py-2 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'repeat password',
        'class': 'w-full py-2 rounded-xl'
    }))
    

class TravelSearchForm(forms.Form):
    source = forms.CharField(label="Source")
    destination = forms.CharField(label="Destination")


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["number_of_seats"]
