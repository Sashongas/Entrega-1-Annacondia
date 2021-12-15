from django.db import models

# Create your models here.
class Pelicula(models.Model):
    tituloPeli = models.CharField(max_length=50)
    generoPeli = models.CharField(max_length=50)
    anioEstrenoPeli = models.IntegerField()

class Serie(models.Model):
    tituloSerie = models.CharField(max_length=50)
    generoSerie = models.CharField(max_length=50)
    anioEstrenoSerie = models.IntegerField()

class Documental(models.Model):
    tituloDoc = models.CharField(max_length=50)
    generoDoc = models.CharField(max_length=50)
    anioEstrenoDoc = models.IntegerField()
