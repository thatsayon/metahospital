from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm, PatientUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from appoinment.models import Appointment
from doctor.models import Doctor

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect


class UserRegistrationViwe(FormView):
    template_name = 'user_registration_patient.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        token = default_token_generator.make_token(user)
        print("token ", token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print("uid ", uid)
        confirm_link = f"https://meta-hospital.onrender.com/patient/active/{uid}/{token}/"
        email_subject = "Confirm Your Email"
        email_body = render_to_string(
            'confirm_email.html', {'confirm_link': confirm_link})

        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return super().form_valid(form)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except (User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class PatientAccountUpdate(View):
    template_name = 'profile.html'

    def get(self, request):
        form = PatientUpdateForm(instance=request.user)
        try:
            doctor = Doctor.objects.get(user=request.user)
            appointments = Appointment.objects.filter(
                doctor=doctor
            )
            context = {'form': form, 'appointments': appointments}
        except ObjectDoesNotExist:
            context = {'form': form, 'appointments': None}
        return render(request, self.template_name, context)

    def post(self, request):
        form = PatientUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        context = {'form': form, 'name': 'ayon'}
        return render(request, self.template_name, context)
