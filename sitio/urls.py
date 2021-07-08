from django.urls import path
from . import views

app_name = "sitio"
urlpatterns = [
    path('', views.index, name="index"),
    path('filtro_secciones/<int:seccion_id>', views.filtro_secciones, name="filtro_secciones"),
    path('<int:articulo_id>', views.articulo, name="articulo"),
    path('articulo_alta', views.articulo_alta, name="articulo_alta"),
    path('articulo_editar/<int:articulo_id>', views.articulo_editar, name="articulo_editar"),
    path('articulo_eliminar/<int:articulo_id>', views.articulo_eliminar, name="articulo_eliminar"),
    path('carrito/<int:articulo_id>', views.carrito, name="carrito"),
    path('carrito_us',views.carrito_us, name="carrito_us"),
]