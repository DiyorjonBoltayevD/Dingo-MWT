from django import forms
from django.contrib.auth.models import User

from dingoapp.models import BookingModel


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "calss": "form-control",
                "placeholder": "Name *"
            }),
            "email": forms.TextInput(attrs={
                "calss": "form-control",
                "placeholder": "Email"
            }),
            "num_of_g": forms.TextInput(attrs={
                "calss": "form-control",
                "placeholder": "Number of guests *",
                "type": "number"
            }),
            "date": forms.TextInput(attrs={
                "calss": "form-control",
                "placeholder": "Date * (yyyy.mm.dd)",
            }),
            "time": forms.TextInput(attrs={
                "calss": "form-control",
                "placeholder": "Time *",
            }),
            "note": forms.Textarea(attrs={
                "calss": "form-control",
                "id": "Textarea",
                "rows": "4",
                "placeholder": "Your Note *",
            }),
            "phone_number": forms.TextInput(attrs={
                "calss": "form-control",
                "placeholder": "Phone number *"
            })
        }


class LoginForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'password']
        model = User
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'single-input',
                'placeholder': 'Username',
            }),
            'password': forms.TextInput(attrs={
                'class': 'single-input',
                'placeholder': 'Password',
                'type': 'password',
            })
        }
