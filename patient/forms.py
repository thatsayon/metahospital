from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=True)
        user.is_active = False
        if commit == True:
            user.save()
            Patient.objects.create(
                user=user
            )
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({

                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
