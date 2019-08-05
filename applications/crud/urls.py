from django.conf.urls import url
from applications.crud import views
from django.urls import path, re_path

app_name = 'crud'

urlpatterns=[
    url(r'^$',views.listado,name='listado'),

    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('postres/', views.PostresListado.as_view(template_name = "postres/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('postres/detalle/<int:pk>', views.PostreDetalle.as_view(template_name = "postres/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('postres/crear', views.PostreCrear.as_view(template_name = "postres/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('postres/editar/<int:pk>', views.PostreActualizar.as_view(template_name = "postres/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('postres/eliminar/<int:pk>', views.PostreEliminar.as_view(), name='eliminar'),    
]