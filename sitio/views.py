from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import Articulo, Seccion
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.

def index(request):
    if "carrito" not in request.session:
        request.session["carrito"] = []
    return render(request,"blog/index.html", {
        "lista_articulos": Articulo.objects.all().order_by("fecha_publicacion")[:10],
        "lista_secciones": Seccion.objects.all(),
        "carrito": request.session["carrito"],
    })

def articulo(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    return render(request, "blog/articulo.html", {
        "articulo": un_articulo
    })

def articulo_alta(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormArticulo(request.POST, request.FILES, instance=Articulo(imagen=request.FILES['imagen'], publicador=user))      
        if form.is_valid():
            form.save()
            return redirect("sitio:index")          
    else:
        form = FormArticulo(initial={'fecha_publicacion':timezone.now()})
        return render(request, "blog/articulo_nuevo.html", {
            "form": form
        })

def articulo_editar(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == "POST":  
        user = User.objects.get(username=request.user)   
        un_articulo.publicador = user
        form = FormArticulo(data=request.POST, files=request.FILES, instance=un_articulo)
        if form.is_valid():
            form.save()
            return redirect("sitio:index")
    else:
        form = FormArticulo(instance = un_articulo)
        return render(request, 'blog/articulo_edicion.html', {
            "articulo": un_articulo,
            "form": form
        })

def articulo_eliminar(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    un_articulo.delete()
    return redirect("sitio:index")

def eliminar(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    un_articulo.delete()
    return redirect("sitio:index")


def filtro_secciones(request, seccion_id):
    una_seccion = get_object_or_404(Seccion, id=seccion_id)
    queryset = Articulo.objects.all()
    queryset = queryset.filter(seccion=una_seccion)
    return render(request,"blog/index.html", {
        "lista_articulos": queryset,
        "lista_secciones": Seccion.objects.all(),
        "seccion_seleccionada": una_seccion
    })

def carrito_us(request):
    return  render(request,"blog/carrito_us.html")

@login_required
def carrito(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    for id in request.session["carrito"]:
        if id == articulo_id:
            #existe el articulo
            return HttpResponseRedirect(reverse("sitio:articulo", args=(un_articulo.id,)))            
    request.session["carrito"] += [articulo_id]
    return HttpResponseRedirect(reverse("sitio:articulo", args=(un_articulo.id,)))   
    
