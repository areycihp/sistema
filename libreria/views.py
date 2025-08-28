#Creacion de la vista
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    # return HttpResponse("Bienvenido bro") #Imprime solo el texto
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html') #Busca el HTML

def libros(request):
    return render(request, 'libros/index.html')

def crear(request):
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')
