from django.urls import path
from ProduccionesTrukiniApp import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
 ]