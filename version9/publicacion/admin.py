from django.contrib import admin
from .models import publicacion
# Register your models here.
class muestra(admin.ModelAdmin):
    list_display=('id', 'titulo', 'resumen_contenido', 'fecha_creacion', 'autor')
    list_filter = ('fecha_creacion', 'autor',)

admin.site.register(publicacion, muestra)