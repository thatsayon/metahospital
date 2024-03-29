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

    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2',
                  'email', 'specialization', 'availabletime', 'image']

    def save(self, commit=True):
        user = super().save(commit=True)
        user.is_active = False
        if commit == True:
            user.save()
            specialization = self.cleaned_data.get('specialization')
            availabletime = self.cleaned_data.get('availabletime')
            image = self.cleaned_data.get('image')

            doctor = Doctor.objects.create(
                user=user,
                fee=0,
                meet_link="",
                image=image,
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


class DoctorUpdateForm(forms.ModelForm):
    availabletime = forms.ModelChoiceField(
        queryset=AvailableTime.objects.all(),
        empty_label="Select an availabletime"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

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

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
