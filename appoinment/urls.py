from django.urls import path
from . import views

urlpatterns = [
    path('<int:doctor_id>/', views.book_appointment, name='appointment'),
]
