
from django.urls import path
from .views import doctors

urlpatterns = [
    path('', doctors),
]
