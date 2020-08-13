from django.urls import path
from CortosApp import views

urlpatterns = [
    path('cortos', views.cortos, name='Cortos'),
    path('cortos/cazador_la_desgracia_de_la_vida', views.desgracia, name='Desgracia'),
    path('cortos/esto_no_es_un_capitulo', views.capitulo, name='Capitulo'),
    path('cortos/cortitos_para_las_fiestas', views.cortitos, name='Cortitos'),
    path('cortos/espacio_publicitario', views.espacio, name='Espacio'),
    path('cortos/servilletas_negras', views.servilletas, name='Servilletas'),
    path('cortos/perdonen_esto_tampoco_es_un_capitulo', views.perdonen, name='Perdonen'),
    path('cortos/la_marmota_fernando', views.marmota, name='Marmota'),
    path('cortos/la_muerte', views.muerte, name='Muerte'),
    path('cortos/esotericos', views.esotericos, name='Esotericos'),
    path('cortos/efemerides', views.efemerides, name='Efemerides'),
    path('cortos/niños', views.ninos, name='Ninos'),
    path('cortos/publicidad_de_actimia', views.publicidad, name='Publicidad'),
    path('cortos/ay_mamberto', views.mamberto, name='Mamberto'),
    path('cortos/charles_bukowski', views.charles, name='Charles'),
 ]