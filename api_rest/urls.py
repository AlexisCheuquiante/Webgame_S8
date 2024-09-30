from django.urls import path
from .import views

urlpatterns = [
    path ('cliente/', views.lista_cliente, name="lista_cliente"),
    path ('cliente/<id_cliente>/', views.vista_cliente, name="vista_cliente"),
    path ('juego/', views.lista_juego, name="lista_juego"),
    path ('juego/<id_juego>/', views.vista_juego, name="vista_juego"),
]