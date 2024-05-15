from django.shortcuts import render, redirect
from .models import Libro, Autor
from .forms import LibroForm, AutorForm
from .utils import ejecutar_consulta_raw


# READ 
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libro/listar_libros.html', {'libros': libros})

# CREATE
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libro/crear_libro.html', {'form': form})

# UPDATE
def actualizar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro/actualizar_libro.html', {'form': form})

# DELETE
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libro/eliminar_libro.html', {'libro': libro})

# CREATE 
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'form': form})

# READ 
def consultar_libros(request):
    consulta = "SELECT * FROM Libro_Libro"
    libros = ejecutar_consulta_raw(consulta)
    return render(request, 'libro/consultar_libros.html', {'libros': libros})