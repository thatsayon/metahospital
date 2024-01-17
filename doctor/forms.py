from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor, Specialization, AvailableTime
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    specialization = forms.ModelChoiceField(
        queryset=Specialization.objects.all(),
        empty_label="Select a specialization"
    )
    availabletime = forms.ModelChoiceField(
        queryset=AvailableTime.objects.all(),
        empty_label="Select an availabletime"
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email', 'specialization', 'availabletime']

    def save(self, commit=True):
        user = super().save(commit=True)
        if commit == True:
            user.save()
            specialization = self.cleaned_data.get('specialization')
            availabletime = self.cleaned_data.get('availabletime')

            doctor = Doctor.objects.create(
                user=user,
                fee=0,
                meet_link="",
            )
            doctor.specialization.set([specialization.id])
            doctor.available_time.set([specialization.id])

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
