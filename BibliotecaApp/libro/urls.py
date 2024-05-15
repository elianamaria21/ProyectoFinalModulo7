from django.urls import path
from . import views

urlpatterns = [
    path('listar-libros/', views.listar_libros, name='listar_libros'),
    path('consultar-libros/', views.consultar_libros, name='consultar_libros'),
    path('crear-libro/', views.crear_libro, name='crear_libro'),
    path('actualizar-libro/<int:id>/', views.actualizar_libro, name='actualizar_libro'),
    path('eliminar-libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
]