from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Editorial(models.Model):
	nombre = models.CharField(max_length=40)
	direccion = models.TextField(null = True, blank = True)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Autor(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)	

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)

@python_2_unicode_compatible
class Area(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Edicion(models.Model):
	edicion = models.CharField(max_length=30)

	def __str__(self):
		return self.edicion


@python_2_unicode_compatible
class Idioma(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre	


@python_2_unicode_compatible
class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	plazo_dias = models.IntegerField()

	def __str__(self):
		return self.nombre				

@python_2_unicode_compatible
class Libro(models.Model):
	cod_libro = models.CharField(max_length=15,primary_key=True)
	portada = models.ImageField(upload_to = 'media/portada')
	editorial = models.ForeignKey(Editorial, null = True)
	autor = models.ForeignKey(Autor)
	area = models.ForeignKey(Area)
	idioma	= models.ForeignKey(Idioma)
	titulo = models.CharField(max_length=100)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	edicion = models.ForeignKey(Edicion)
	categoria = models.ForeignKey(Categoria)
	codigo_dewey = models.DecimalField(blank=True, max_digits=10, decimal_places=5)
	codigo_cutter = models.CharField(max_length=50)
	palabras_claves = models.CharField(max_length=500)

	def __str__(self):
		return self.titulo		

@python_2_unicode_compatible
class CopiaLibro(models.Model):
	cod_copia =  models.CharField(max_length=15,primary_key=True)
	cod_libro = models.ForeignKey(Libro)
	reservado = models.BooleanField()
	

	def __str__(self):
		return self.cod_copia

@python_2_unicode_compatible
class Carrera(models.Model):
	carrera = models.CharField(max_length=100)
	numPrestamos = models.IntegerField(null = True)	

	def __str__(self):
		return self.carrera

class Perfil(User):
	numero_telefono = models.IntegerField()
	carrera = models.ForeignKey(Carrera)

	def __int__(self):
		return self.numero_telefono

		

@python_2_unicode_compatible
class Reservacion(models.Model):
	cod_copia = models.ForeignKey(CopiaLibro)
	cod_libro = models.CharField(max_length=15)
	numero_cuenta = models.ForeignKey(Perfil)
	nombre = models.CharField(max_length=100)
	fecha_reservacion = models.DateTimeField()
	fecha_prestamo = models.DateTimeField(null=True)
	fecha_entrega = models.DateTimeField(null=True)
	comentario = models.CharField(max_length=300, null = True)
	prestado = models.BooleanField()
	plazo_dias = models.IntegerField()

	def __str__(self):
		return unicode(self.cod_copia)

@python_2_unicode_compatible
class Prestamo(models.Model):
	cod_copia = models.ForeignKey(CopiaLibro)
	cod_libro = models.CharField(max_length=15)
	numero_cuenta = models.ForeignKey(Perfil)
	nombre = models.CharField(max_length=100)
	fecha_prestamo = models.DateTimeField(null=True)
	fecha_entrega = models.DateTimeField(null=True)
	plazo_dias = models.IntegerField()

	def __str__(self):
		return unicode(self.cod_copia)		


@python_2_unicode_compatible
class Administrador(models.Model):
	numero_cuenta = models.ForeignKey(Perfil)

	def __str__(self):
		return self.numero_cuenta