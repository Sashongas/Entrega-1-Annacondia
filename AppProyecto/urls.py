from django.urls import path
from AppProyecto import views

urlpatterns = [
    path('inicio', views.inicio, name = "Inicio"),
    path('pelicula', views.pelicula, name = "Pelicula"),
    path('serie', views.serie, name = "Serie"),
    path('documental', views.documental, name = "Documental")
]