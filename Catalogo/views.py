#coding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from .forms import RegistroForm
from .models import *
from itertools import chain
from django.db.models.functions import Concat
from django.db.models import Q, Count
from django.db.models import Value
import datetime

@login_required()
def busqueda(request):
	nombrearea = Categoria.objects.all()
	query = request.GET.get("q")
	nombrear = request.GET.get("dropdown1")
	user = request.user
	if str(user) == 'admin':
		admin = True
	else:	
		admin = False

	if nombrear != "" and query == "":
		if nombrear == "Todas las categorias":
			libros = Libro.objects.all().order_by('-fecha_registro')
			nombrearea = Categoria.objects.exclude(nombre=nombrear)
		else:
			libros=Libro.objects.filter(Q(categoria__nombre__iexact=nombrear))
			nombrearea = Categoria.objects.exclude(nombre=nombrear)
		return render(request, 'busqueda.html', {'libros': libros, 'nombrearea': nombrearea, 'user': admin,})
	elif query != "" and nombrear == "":
		if query:
			libros=Libro.objects.annotate(nombrecompleto = Concat('autor__nombre', Value(' '), 'autor__apellido'),).filter(Q(titulo__icontains=query) | 
				Q(autor__nombre__icontains = query) | Q(autor__apellido__icontains=query) | Q(nombrecompleto__icontains = query) | Q(palabras_claves__icontains = query))
		return render(request, 'busqueda.html', {'libros': libros, 'nombrearea': nombrearea, 'user': admin,})
	elif query != "" and nombrear != "":
		if nombrear == "Todas las areas":
			libros=Libro.objects.annotate(nombrecompleto = Concat('autor__nombre', Value(' '), 'autor__apellido'),).filter(Q(titulo__icontains=query) | 
			Q(autor__nombre__icontains = query) | Q(autor__apellido__icontains=query) | Q(nombrecompleto__icontains = query) | Q(palabras_claves__icontains = query))
		else:
			libros=Libro.objects.annotate(nombrecompleto = Concat('autor__nombre', Value(' '), 'autor__apellido'),).filter(Q(categoria__nombre__iexact=nombrear) & (Q(titulo__icontains=query) | 
			Q(autor__nombre__icontains = query) | Q(autor__apellido__icontains=query) | Q(nombrecompleto__icontains = query) | Q(palabras_claves__icontains = query)))
		nombrearea = Categoria.objects.exclude(nombre=nombrear)
		return render(request, 'busqueda.html', {'libros': libros, 'nombrearea': nombrearea, 'user': admin,})
	elif nombrear == "" and query == "":
		return HttpResponseRedirect(reverse('index'))

@login_required()
def busRes(request):
	query = request.GET.get("que")
	copias_libro = CopiaLibro.objects.all()
	libros = Libro.objects.all()
	user = request.user
	if query == "":
		res = Reservacion.objects.all().select_related()
	if query:
		res=(Reservacion.objects.filter(nombre__icontains=str(query))| Reservacion.objects.filter(numero_cuenta__username__icontains = query) | Reservacion.objects.filter(cod_copia__cod_copia__icontains = query) | Reservacion.objects.filter(cod_libro__icontains=str(query)))
	
	if str(user) == 'admin':
		admin = True
	else:	
		admin = False
	return render(request, 'reservaciones.html', {'user': admin, 
												  'res': res,
												  'cop': copias_libro,
												  'libros': libros,})


@login_required()
def reservaciones(request):
	res = Reservacion.objects.all().select_related()
	copias_libro = CopiaLibro.objects.all()
	libros = Libro.objects.all()

	user = request.user
	#if res.prestado == False:
	#	prestado = False
	#else:
	#	prestado = True

	if str(user) == 'admin':
		admin = True
	else:	
		admin = False

	now = datetime.datetime.now()	
	return render(request, 'reservaciones.html', {'user': admin, 
												  'now': now,
												  'res': res,
												  'cop': copias_libro,
												  'libros': libros})
												 # 'prestado': prestado})

@login_required()
def estadisticas(request):

	users = len(Perfil.objects.all())
	res = Reservacion.objects.all()
	pres = Reservacion.objects.filter(prestado=True)
	dis = CopiaLibro.objects.filter(reservado=False)
	ed = len(Editorial.objects.all())
	copias_libro = CopiaLibro.objects.all()
	libros = Libro.objects.all()
	clibros = len(libros)
	prestados = len(pres)
	disponibles = len(dis)
	reser = len(res)
	#comp = len(Prestamo.objects.filter(numero_cuenta__carrera = Carrera.objects.get(id=1)))
	c = Carrera.objects.all
	maxi = Prestamo.objects.values('cod_libro').annotate(dcount=Count('cod_libro')).order_by('-dcount')[:5]
	alumnos = Prestamo.objects.values('nombre').annotate(acount=Count('cod_libro')).order_by('-acount')[:3]


	user = request.user
	#if res.prestado == False:
	#	prestado = False
	#else:
	#	prestado = True

	if str(user) == 'admin':
		admin = True
	else:	
		admin = False
	return render(request, 'estadisticas.html', {'user': admin, 
												  'res': res,
												  'cop': copias_libro,
												  'clibros': clibros,
												  'prestados': prestados,
												  'disponibles': disponibles,
												  'reser':reser,
												  'users': users,
												  'c':c,
												  'ed':ed,
												  'maxi':maxi,
												  'alumnos': alumnos})
												 # 'prestado': prestado})												 

@login_required()
def index(request):
		user = request.user
		if str(user) == 'admin':
			admin = True
		else:	
			admin = False	
		libros = Libro.objects.all().order_by('-fecha_registro')[:8]
		literatura = Libro.objects.filter(categoria__nombre__iexact='Literatura').order_by('-fecha_registro')[:8]
		motivacional = Libro.objects.filter(categoria__nombre__iexact='Lectura Motivacional').order_by('-fecha_registro')[:8]
		m = Categoria.objects.get(nombre='Lectura Motivacional')
		general = Libro.objects.filter(categoria__nombre__iexact='Coleccion General').order_by('-fecha_registro')[:8]
		referencia = Libro.objects.filter(categoria__nombre__iexact='Coleccion referencia').order_by('-fecha_registro')[:8]
		espiritual = Libro.objects.filter(categoria__nombre__iexact='Lectura Espiritual').order_by('-fecha_registro')[:8]
		nombrearea = Categoria.objects.all()
		return render(request, 'index.html', {'libros': libros, 
											  'nombrearea': nombrearea, 
											  'user': admin,
											  'literatura': literatura,
											  'motivacional': motivacional,
											  'general': general,
											  'referencia': referencia,
											  'espiritual': espiritual,
											  'm':m
											  })				
@login_required()
def ver_mas(request, idc):		
	libros = Libro.objects.filter(categoria__nombre__iexact	 = idc)
	return render(request, 'ver_mas.html', {'libros': libros,})			

@login_required()
def ver_mas_motivacional(request):		
	libros = Libro.objects.filter(categoria__nombre__iexact	 = 'Lectura Motivacional')
	return render(request, 'ver_mas.html', {'libros': libros,})		

@login_required()
def ver_mas_general(request):		
	libros = Libro.objects.filter(categoria__nombre__iexact	 = 'Coleccion General')
	return render(request, 'ver_mas.html', {'libros': libros,})	

@login_required()
def ver_mas_referencia(request):		
	libros = Libro.objects.filter(categoria__nombre__iexact	 = 'Coleccion Referencia')
	return render(request, 'ver_mas.html', {'libros': libros,})	

@login_required()
def ver_mas_espiritual(request):		
	libros = Libro.objects.filter(categoria__nombre__iexact	 = 'Lectura espiritual')
	return render(request, 'ver_mas.html', {'libros': libros,})	



@login_required()
def cancelar(request, idr):
	r = Reservacion.objects.get(id = idr)
	copia = CopiaLibro.objects.get(cod_copia = r.cod_copia)
	copia.reservado = False
	copia.save()
	r.delete()

	return render(request, 'reservaciones.html', {'res': res, 'cop':cop})		

@login_required()
def reservacion(request, idl):
	libro = Libro.objects.get(pk=idl)
	copias = CopiaLibro.objects.filter(cod_libro = idl)
	copias_disponibles = copias.filter(reservado=False)
	numero_copias = copias_disponibles.count()
	numero_cuenta = Perfil.objects.get(username=request.user)
	res = Reservacion.objects.filter(numero_cuenta = numero_cuenta)
	reservaciones_usuario = Reservacion.objects.filter(numero_cuenta = numero_cuenta)



	if numero_copias <= 0:
		n_copias = 'No hay copias disponibles de este libro.'
		disponible = False
	else:
		if res.count() >=3:
			n_copias = 'No puede reservar este libro porque ha excedido el límite de libros por alumno.'
			disponible = False
		else:
			n_copias = numero_copias
			disponible = True
		for r in reservaciones_usuario:
			if str(r.cod_libro) == str(libro):	
				n_copias = 'Ya ha reservado una copia de este libro.'
				disponible = False
			
	
	return render(request, 'reservacion.html', {'libro': libro, 
												'numero_copias': n_copias,
												'disponible': disponible})

@login_required()
def confirmar_reservacion(request, idl):
	if request.method == 'POST':
		copia = CopiaLibro.objects.filter(cod_libro=idl)
		cod_copia = CopiaLibro.objects.get(cod_copia=copia[0])
		libro = Libro.objects.get(cod_libro=idl)
		comentario = request.POST.get('comentario')
		now = datetime.datetime.now()
		cat = Categoria.objects.get(nombre=libro.categoria)
		#dias = datetime.timedelta(days=cat.plazo_dias)
		#fecha_entrega = now+dias
		perfil = Perfil.objects.get(username=request.user)
	    	nombre = perfil.first_name + ' ' + perfil.last_name
		c = CopiaLibro.objects.get(cod_copia = cod_copia)
		c.reservado = True;
		c.save()
		titulo = 'Se ha realizado con éxito la reservación del libro'
		msj = 'Debera de ir a traerlo a la biblioteca de la universidad, en caso de que no lo se presente en las proximas 24 horas, la reservacion sera cancelada.'

		r = Reservacion(cod_copia = cod_copia,
						numero_cuenta = perfil,
						fecha_reservacion = now,
						nombre = str(nombre),
						comentario = comentario,
						cod_libro = libro,
						prestado = False,
						plazo_dias = cat.plazo_dias)
		r.save()
						 
		return render(request, 'reservacion.html', {'libro': libro,
													'titulo': titulo, 
												    'msj': msj,
												    'disponible': False})

@login_required()
def quitar(request, idr):

	r = Reservacion.objects.get(id = idr)
	copia = CopiaLibro.objects.get(cod_copia=r.cod_copia)
	copia.reservado = False;
	copia.save()
	r.delete()
	
	return HttpResponseRedirect(reverse('reservaciones'))	

@login_required()
def entregar(request, idr):

	r = Reservacion.objects.get(id = idr)
	copia = CopiaLibro.objects.get(cod_copia=r.cod_copia)
	copia.reservado = False;
	copia.save()
	r.delete()
	
	return HttpResponseRedirect(reverse('reservaciones'))	

@login_required()
def prestar(request, idr):

	r = Reservacion.objects.get(id = idr)
	cod_copia = r.cod_copia
	nombre = r.nombre
	libro = Libro.objects.get(titulo = r.cod_libro)
	cat = Categoria.objects.get(nombre = libro.categoria)
	now = datetime.datetime.now()
	dias = datetime.timedelta(days = r.plazo_dias)
	fecha_entrega = now + dias
	perfil = Perfil.objects.get(username = r.numero_cuenta)
	carrera = Carrera.objects.get(carrera = perfil.carrera)
	carrera.numPrestamos = int(carrera.numPrestamos) + 1
	carrera.save()
	r.fecha_prestamo = now
	r.fecha_entrega = fecha_entrega
	r.prestado = True;
	r.save()

	p = Prestamo(cod_copia = cod_copia,
				numero_cuenta = perfil,
				fecha_entrega = fecha_entrega,
				fecha_prestamo = now,
				nombre = str(nombre),
				cod_libro = libro,
				plazo_dias = cat.plazo_dias)

	p.save()
	
	return HttpResponseRedirect(reverse('reservaciones'))		

class RegistroUsuario(CreateView):
	
	model = Perfil
	template_name = 'registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('form_login')
	





