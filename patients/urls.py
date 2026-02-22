
from django.urls import path
from .views import patients

urlpatterns = [
    path('', patients),
]
