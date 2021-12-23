from django import forms

from .models import User

class NoticiaForm(forms.ModelForm):
	class Meta:
		model= User
		fields = ('first_name', 'last_name', 'email', 'password')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)