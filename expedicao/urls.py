from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.lista_carregamentos, name='home'),  
    path('carregamentos/', views.lista_carregamentos, name='lista_carregamentos'),
    path('adicionar/', views.adicionar_carregamento, name='adicionar_carregamento'),
    path('relatorio/', views.relatorio_analitico, name='relatorio_analitico'),
    path('detalhes/<int:id>/', views.detalhes_carregamento, name='detalhes_carregamento'),
]