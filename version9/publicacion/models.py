from django.db import models
from django.db.models.lookups import Range
from django.utils import timezone
from user.models import User
# Create your models here.
class publicacion(models.Model):
    titulo=models.CharField(max_length=20)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    resumen_contenido=models.CharField(max_length=30, null=True)
    contenido=models.CharField(max_length=200)
    fecha_creacion=models.DateField(timezone.now)
    tema_entre1y17=models.CharField(max_length=2, blank=True, null=True)
    clase=models.CharField(max_length=10, blank=True, null=True)

    
   
 #------------------------------------------------------------------  
   
   
    def publicar(self):
        self.fecha_publicacion= timezone.now()
        self.save()
    def borrar(self):
        self.delete()
#-______________--------------------------------------------------------------------
    
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name =("publicacion")
        verbose_name_plural =("publicaciones")

class Comentario(models.Model):
	noticia = models.ForeignKey(publicacion, on_delete= models.CASCADE)
	contenido = models.TextField()
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha_hora = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.contenido

	class Meta:
		verbose_name = ("Comentario")
		verbose_name_plural= ("Comentarios")