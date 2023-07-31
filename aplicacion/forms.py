from django import forms

class ZonaNorteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)
    
class ZonaOesteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)

class ZonaSurForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)

class CabaForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)