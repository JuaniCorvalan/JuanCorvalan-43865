from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# Create your views here.
def paginaprincipal(request):
    return render(request, "aplicacion/paginaprincipal.html")

class ZonaNorteList(LoginRequiredMixin, ListView):
    model = ZonaNorte

class ZonaOesteList(LoginRequiredMixin, ListView):
    model = ZonaOeste
    
class ZonaSurList(LoginRequiredMixin, ListView):
    model = ZonaSur

class CabaList(LoginRequiredMixin, ListView):
    model = Caba
        
class ZnCreate(LoginRequiredMixin, CreateView):
    model = ZonaNorte
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona norte')

class ZoCreate(LoginRequiredMixin, CreateView):
    model = ZonaOeste
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona oeste')
    
class ZsCreate(LoginRequiredMixin, CreateView):
    model = ZonaSur
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona sur')
    
class CabaCreate(LoginRequiredMixin, CreateView):
    model = Caba
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('caba')
    
class ZnDetail(LoginRequiredMixin, DetailView):
    model = ZonaNorte

class ZoDetail(LoginRequiredMixin, DetailView):
    model = ZonaOeste 

class ZsDetail(LoginRequiredMixin, DetailView):
    model = ZonaOeste

class CabaDetail(LoginRequiredMixin, DetailView):
    model = Caba
    
class ZnUpdate(LoginRequiredMixin, UpdateView):
    model = ZonaNorte
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona norte')
    
class ZoUpdate(LoginRequiredMixin, UpdateView):
    model = ZonaOeste
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona oeste')
    
class ZsUpdate(LoginRequiredMixin, UpdateView):
    model = ZonaSur
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('zona sur')
    
class CabaUpdate(LoginRequiredMixin, UpdateView):
    model = Caba
    fields = ['nombre', 'localidad', 'telefono', 'deporte']
    success_url = reverse_lazy('caba')
    
class ZnDelete(LoginRequiredMixin, DeleteView):
    model = ZonaNorte
    success_url = reverse_lazy('zona norte')

class ZoDelete(LoginRequiredMixin, DeleteView):
    model = ZonaOeste
    success_url = reverse_lazy('zona oeste')

class ZsDelete(LoginRequiredMixin, DeleteView):
    model = ZonaSur
    success_url = reverse_lazy('zona sur')

class CabaDelete(LoginRequiredMixin, DeleteView):
    model = Caba
    success_url = reverse_lazy('caba')

@login_required
def znbuscar(request):
    return render(request, "aplicacion/znbuscar.html")

def znbuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/znresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})

@login_required
def zobuscar(request):
    return render(request, "aplicacion/zobuscar.html")

@login_required
def zobuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/zoresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})

@login_required
def zsbuscar(request):
    return render(request, "aplicacion/zsbuscar.html")

@login_required
def zsbuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/zsresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})

@login_required
def zobuscar(request):
    return render(request, "aplicacion/zobuscar.html")

@login_required
def zobuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/zoresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})

@login_required
def cababuscar(request):
    return render(request, "aplicacion/cababuscar.html")

@login_required
def cababuscar2(request):
    if request.GET['localidad']:
        localidad = request.GET['localidad']
        zona_norte = ZonaNorte.objects.filter(localidad__icontains=localidad)
        return render(request, 
                      "aplicacion/cabaresultados.html", 
                      {"localidad":localidad, "nombres": zona_norte})
        
        
def log_in(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).image.url
                except:
                    avatar= '/media/avatares/default.jpeg'
                finally:
                    request.session['avatar']=avatar
                return render(request, "aplicacion/paginaprincipal.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": f"Datos incorrectos"})
        else: 
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": f"Datos incorrectos"})
    
    
    miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {"form":miForm})


def register(request):
    if request.method == "POST":
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/paginaprincipal.html", {"mensaje": "Registro exitoso"})
        
    else:
        form = RegistroUsuariosForm()
        
    return render(request, "aplicacion/registro.html", {"form": form})

@login_required
def user_edit(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.password1 = form.cleaned_data.get('password1') 
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.save()
            return render(request, "aplicacion/paginaprincipal.html", {"mensaje": f"{usuario.username} se ha actualizado correctamente"})            
        else:
            return render(request, "aplicacion/editar_form.html", {'form: form'}) 
    else:
        form = UserEditForm(instance = usuario)           
    return render(request, "aplicacion/editar_form.html", {'form': form, 'usuario': usuario})
    
@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            avatar=Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url 
            request.session['avatar']= imagen 

                
            return render(request, "aplicacion/paginaprincipal.html")
    else:
        form= AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {"form": form})


#-----------------------------------------------------

def comentariozn(request, zona_norte_id):
    zona_norte = ZonaNorte.objects.get(pk=zona_norte_id)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.zona_norte = zona_norte
            comentario.autor = request.user
            comentario.save()
            return redirect('detail_zonanorte', pk=zona_norte_id)

    else:
        form = ComentarioForm()
    
    comentarios = zona_norte.comentarios.all()
    return render(request, 'aplicacion/comentariozn.html', {'form': form, 'comentarios': comentarios, 'zona_norte': zona_norte})



