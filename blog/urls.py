# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_entradas, name='lista_entradas'),
]
