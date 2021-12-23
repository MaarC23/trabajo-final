from django.urls import path
from django.views.generic.base import View

from . import views
from .views import Detalle, borrarpublicacion, Updatepublicacion
urlpatterns = [
    path('saludo', views.saludo, name='index'),
    path('', views.Listar.as_view(), name='lista'),
    path("explicacion/", views.quees19.as_view(), name="explicacion"),
    path('crear/', views.Crearpublicacion.as_view(), name='crear'),    
    path('detalle/<slug:pk>',Detalle.as_view(), name='detalle'),
    path('update/<slug:pk>', Updatepublicacion.as_view(), name='actualizar'),
    path('borrar/<slug:pk>' , borrarpublicacion.as_view(), name='borrar')

        
]