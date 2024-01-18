from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import UserRegistrationForm, DoctorUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from .models import Doctor
from appoinment.models import Appointment, Review
from patient.models import Patient
from appoinment.forms import ReviewForm
from django.http import HttpResponseRedirect


class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "user_login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("home")


class DoctorDetailView(TemplateView):
    template_name = 'detail.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('id')
        context['doctor'] = Doctor.objects.get(pk=id)
        patient, created = Patient.objects.get_or_create(
            user=self.request.user)
        context['can_review'] = Appointment.objects.filter(
            doctor=Doctor.objects.get(pk=id),
            patient=patient
        ).exists()
        context['review_form'] = self.form_class()
        try:
            appointment = Appointment.objects.get(
                doctor=Doctor.objects.get(pk=id),
                patient=patient
            )
            reviews = Review.objects.filter(appointment=appointment)
            context['reviews'] = reviews
        except Exception:
            context['reviews'] = None
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            id = self.kwargs.get('id')
            doctor = Doctor.objects.get(pk=id)
            patient, created = Patient.objects.get_or_create(
                user=self.request.user)
            appointment = Appointment.objects.get(
                doctor=doctor,
                patient=patient
            )
            form.save(appointment=appointment)
            return HttpResponseRedirect(reverse_lazy('detail', kwargs={'id': id}))
        return render(request, self.template_name, {'review_form': form})

    def get_success_url(self):
        id = self.kwargs.get('id')
        return reverse_lazy('doctor_detail', kwargs={'id': id})


class DoctorUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = DoctorUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DoctorUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
