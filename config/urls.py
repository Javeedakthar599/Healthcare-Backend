
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/auth/register/', include('authentication.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]
