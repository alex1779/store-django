from django.urls import path
from .views import VRegistro, cerrar_session, loguear

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_session', cerrar_session, name="cerrar_sesion"),
    path('loguear', loguear, name="loguear"),
]