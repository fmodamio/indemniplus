from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('', views.enviar_formulario, name='index'),
    path('gracias/', views.gracias, name='index_gracias'),    
    path('legal/', views.legal, name='legal'),
    path('medica/', views.medica, name='medica'),
]
