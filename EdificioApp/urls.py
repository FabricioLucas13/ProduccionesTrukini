from django.urls import path
from EdificioApp import views

urlpatterns = [
    path('el_ultimo_edificio_de_la_cuadra', views.edificio, name='Edificio'),
    path('el_ultimo_edificio_de_la_cuadra/afortunada_desdicha', views.afortunada, name='afortunada'),
    path('el_ultimo_edificio_de_la_cuadra/el_dinero', views.dinero, name='Dinero'),
    path('el_ultimo_edificio_de_la_cuadra/una_nueva_etapa', views.nueva, name='Nueva'),
 ]