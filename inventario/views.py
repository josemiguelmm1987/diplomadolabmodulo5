from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from .serializers import CategoriaSerializer

from .models import Categoria, Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def contact(request, name):
    return HttpResponse(f"Hello, {name}")

# def categorias(request):
#     categorias = Categoria.objects.all()
#     return render(request, "categorias.html", {
#         "categorias": categorias
#     })

def categorias(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    categorias = Categoria.objects.all()
    return render(request, "form_categorias.html", {
        "categorias": categorias
    })

def productoFormView(request):
    # form = ProductoForm(request.POST)
    form = ProductoForm()
    producto = None
    id_producto = request.GET.get('id')

    if id_producto:
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductoForm(instance=producto)

    if request.method == 'POST':
        if producto:
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)
    
    if form.is_valid():
        form.save()
    return render(request, "form_productos.html", {"form": form})

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer