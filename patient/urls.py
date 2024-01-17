from django.urls import path
from .views import UserRegistrationViwe, activate

urlpatterns = [
    path('register/', UserRegistrationViwe.as_view(), name='pregister'),
    path('active/<uid64>/<token>/', activate, name='activate'),
]
