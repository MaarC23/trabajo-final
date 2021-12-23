from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    dni = models.CharField(max_length=8, null=True, blank=True)


    
   
 #------------------------------------------------------------------  
   
   
    def publicar(self):
        
        self.save()
#-______________--------------------------------------------------------------------
    
    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name =("usuario")
        verbose_name_plural =("usuarios")