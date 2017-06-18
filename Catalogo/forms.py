#coding: utf8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil

class RegistroForm(UserCreationForm):
	email = forms.EmailField(required=True)

	def clean_username(self):
		
		if len(str(self.cleaned_data['username'])) != 13:
			raise forms.ValidationError('Número de cuenta inválido.')
	 	else:
			try:
				user = Perfil.objects.get(username = self.cleaned_data['username'])
			except:
				user = 0

			if str(user) == str(self.cleaned_data['username']):
				raise forms.ValidationError('Número de cuenta ya existe.')
			else:
				return self.cleaned_data['username']
	 			
	 		

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		self.base_fields['username'].widget.attrs['class'] = ''
		self.base_fields['numero_telefono'].widget.attrs['class'] = 'form_item'
		self.base_fields['password1'].widget.attrs['class'] = ' form_item'
		self.base_fields['password2'].widget.attrs['class'] = ' form_item'
		self.base_fields['email'].widget.attrs['class'] = ' form_item'
		self.base_fields['first_name'].widget.attrs['class'] = 'form_item'
		self.base_fields['last_name'].widget.attrs['class'] = 'form_item'
		self.base_fields['carrera'].widget.attrs['class'] = ' form_item'
		

	class Meta: 
		model = Perfil
		
		fields =[
			'username',
			'first_name',
			'last_name',
			'numero_telefono',
			'email',
			'carrera'
			]		

		labels = {
			'username': 'Numero de cuenta',
			'first_name': 'Nombre',
			'last_name': 'Apellidos',
			'numero_telefono': 'Numero de telefono',
			'email': 'Correo',
			'carrera': 'Carrera',
			}

		widgets = {
        }		

	
	