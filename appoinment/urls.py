from django.urls import path
from . import views

urlpatterns = [
    path('<int:doctor_id>/', views.book_appointment, name='appointment'),
    path('<int:doctor_id>/<int:patient_id>/',
         views.delete_patient, name='delpat'),
]
