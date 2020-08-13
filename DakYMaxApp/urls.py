from django.urls import path
from DakYMaxApp import views

urlpatterns = [
    path('dakymax', views.dakymax, name='Dakymax'),
    path('dakymax/crono-aventuras', views.temporada1, name='Temporada1'),
    path('dakymax/crono-aventuras/punto_de_partida-llegada', views.llegada, name='Llegada'),
    path('dakymax/crono-aventuras/bucle_imperfecto', views.imperfecto, name='Imperfecto'),
    path('dakymax/crono-aventuras/trenzado', views.trenzado, name='Trenzado'),
 ]