from django import forms

class PeliculaFormulario(forms.Form):
 tituloPeli = forms.CharField(max_length=50)
 generoPeli = forms.CharField(max_length=50)
 anioEstrenoPeli = forms.IntegerField()

class SerieFormulario(forms.Form):
    tituloSerie = forms.CharField(max_length=50)
    generoSerie = forms.CharField(max_length=50)
    anioEstrenoSerie = forms.IntegerField()

class DocumentalFormulario(forms.Form):
    tituloDoc = forms.CharField(max_length=50)
    generoDoc = forms.CharField(max_length=50)
    anioEstrenoDoc = forms.IntegerField()