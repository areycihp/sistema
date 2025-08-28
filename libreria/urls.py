#URLS propias de la aplicacion
from django.urls import path
from . import views

#El usuario accede a la vista
urlpatterns = [
    path('', views.inicio, name='inicio'), #Lleva el view de Inicio
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
] 