from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.
def paginaprincipal(request):
    return render(request, "aplicacion/paginaprincipal.html")

class ZonaNorteList(ListView):
    model = ZonaNorte

class ZonaOesteList(ListView):
    model = ZonaOeste
    
class ZonaSurList(ListView):
    model = ZonaSur

class CabaList(ListView):
    model = Caba
        
class ZnCreate(CreateView):
    model = ZonaNorte
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona norte')

class ZoCreate(CreateView):
    model = ZonaOeste
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona oeste')
    
class ZsCreate(CreateView):
    model = ZonaSur
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona sur')
    
class CabaCreate(CreateView):
    model = Caba
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('caba')
    
class ZnDetail(DetailView):
    model = ZonaNorte

class ZoDetail(DetailView):
    model = ZonaOeste 

class ZsDetail(DetailView):
    model = ZonaOeste

class CabaDetail(DetailView):
    model = Caba
    
class ZnUpdate(UpdateView):
    model = ZonaNorte
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona norte')
    
class ZoUpdate(UpdateView):
    model = ZonaOeste
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona oeste')
    
class ZsUpdate(UpdateView):
    model = ZonaSur
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona sur')
    
class CabaUpdate(UpdateView):
    model = Caba
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('caba')
    
class ZnDelete(DeleteView):
    model = ZonaNorte
    success_url = reverse_lazy('zona norte')

class ZoDelete(DeleteView):
    model = ZonaOeste
    success_url = reverse_lazy('zona oeste')

class ZsDelete(DeleteView):
    model = ZonaSur
    success_url = reverse_lazy('zona sur')

class CabaDelete(DeleteView):
    model = Caba
    success_url = reverse_lazy('caba')
    
def znbuscar(request):
    return render(request, "aplicacion/znbuscar.html")

def znbuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/znresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})

def zobuscar(request):
    return render(request, "aplicacion/zobuscar.html")

def zobuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/zoresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})

def zsbuscar(request):
    return render(request, "aplicacion/zsbuscar.html")

def zsbuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/zsresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})

def zobuscar(request):
    return render(request, "aplicacion/zobuscar.html")

def zobuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/zoresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})
        
def cababuscar(request):
    return render(request, "aplicacion/cababuscar.html")

def cababuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/cabaresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})