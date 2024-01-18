from django.contrib import admin
from django.urls import path, include
from core.views import home
from django.conf import settings
from django.conf.urls.static import static
from patient.views import PatientAccountUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('profile/', PatientAccountUpdate.as_view(), name='profile'),
    path('<slug:specialization_slug>/', home, name="special"),
    path('', home, name="home"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
