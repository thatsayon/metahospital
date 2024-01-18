from django.urls import path
from .views import UserRegistrationViwe, activate, PatientAccountUpdate

urlpatterns = [
    path('register/', UserRegistrationViwe.as_view(), name='pregister'),
    path('active/<uid64>/<token>/', activate, name='activate'),
    # path('profile/', PatientAccountUpdate.as_view(), name='profile'),
]
