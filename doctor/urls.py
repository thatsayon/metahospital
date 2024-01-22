from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, DoctorDetailView, activate

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('detail/<int:id>/', DoctorDetailView.as_view(), name='detail'),
    path('active/<uid64>/<token>/', activate, name='activate'),
]
