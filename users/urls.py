# users/urls.py
from django.urls import path
from .views import CambiarContrasenaView

urlpatterns = [
    path('cambiar-contrasena/', CambiarContrasenaView.as_view(), name='cambiar_contrasena'),
]
