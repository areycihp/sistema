#Creacion de la vista
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido bro") #Imprime solo el texto

def nosotros(request):
    return render(request, 'paginas/nosotros.html') #Busca el HTML