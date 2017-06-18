#coding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyAuthenticationForm
from django.contrib.auth import authenticate, login, logout


def registrar(request):
	form = MyAuthenticationForm()
	return render(request, 'form_registrar.html', {'form': form})


def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/catalogo/')
	form = MyAuthenticationForm()
	user = request.GET.get('user')
	return render(request, 'form_login.html', {'form': form, 'user': user})

def log_out(request):
	logout(request)
	return HttpResponseRedirect("/")

def log_in(request):
	if request.method == 'POST':
		form = MyAuthenticationForm(data=request.POST)

		if form.is_valid():
			user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/catalogo/')
				else:
					return HttpResponse('tu usuario ha sido desactivado')
			else:
				return HttpResponse('Usuario/Contrasenia invalidos')			
		else:
			return render(request, 'form_login.html', {'form': form})			
	else:
		return HttpResponse('No puede ingresar')

		