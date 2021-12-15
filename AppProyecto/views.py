from django.shortcuts import render
from django.http import HttpResponse
from AppProyecto.forms import *
from AppProyecto.models import Pelicula, Documental, Serie

# Create your views here.
def inicio(request):
    return render(request, 'AppProyecto/inicio.html')
    
def pelicula(request):
    
    if request.method == "POST":
     peliInsta = Pelicula(tituloPeli=request.POST["tituloPeli"], generoPeli= request.POST["generoPeli"], anioEstrenoPeli=request.POST["anioEstrenoPeli"])
     peliInsta.save()
     return render(request, 'AppProyecto/inicio.html')

    return render(request, 'AppProyecto/pelicula.html')
        

def serie(request):
    if request.method == "POST":
     serieInsta = Serie(tituloSerie=request.POST["tituloSerie"], generoSerie=request.POST["generoSerie"], anioEstrenoSerie=request.POST["anioEstrenoSerie"])
     serieInsta.save()
     return render(request, 'AppProyecto/inicio.html')
    return render(request, 'AppProyecto/serie.html')

def documental(request):
    if request.method == "POST":
     docInsta = Documental(tituloDoc=request.POST["tituloDoc"], generoDoc=request.POST["generoDoc"], anioEstrenoDoc=request.POST["anioEstrenoDoc"])
     docInsta.save()
     return render(request, 'AppProyecto/inicio.html')
    return render(request, 'AppProyecto/documental.html')
