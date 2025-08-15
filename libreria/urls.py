#URLS propias de la aplicacion
from django.urls import path
from . import views

#El usuario accede a la vista
urlpatterns = [
    path('', views.inicio, name='inicio')
] 