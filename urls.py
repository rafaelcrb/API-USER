from django.urls import path
from .views import UsuarioListView, UsuarioCreateView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario_create'),
]
