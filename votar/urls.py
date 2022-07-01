from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_redirect, name='homepage_redirect'),
    path('votar/', views.votar, name='votar'),
    path('resultado/', views.resultado, name='resultado'),
    path('candidatos/', views.candidatos, name='candidatos')
]