from django import forms

from .models import publicacion

class NoticiaForm(forms.ModelForm):
	class Meta:
		model= publicacion
		fields = ('autor', 'titulo', 'contenido', 'fecha_creacion')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)