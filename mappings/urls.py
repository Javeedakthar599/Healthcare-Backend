
from django.urls import path
from .views import mappings

urlpatterns = [
    path('', mappings),
]
