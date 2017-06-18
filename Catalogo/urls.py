from django.conf.urls import url
from .import views 
from .views import RegistroUsuario

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^busqueda/$', views.busqueda, name='busqueda'),
	url(r'^busRes/$', views.busRes, name='busRes'),
	url(r'^registro_usuario/$', RegistroUsuario.as_view(), name='registro_usuario'),
	url(r'^quitar/(?P<idr>[\w\-]+)/$', views.quitar, name='quitar'),
	url(r'^entregar/(?P<idr>[\w\-]+)/$', views.entregar, name='entregar'),
	url(r'^prestar/(?P<idr>[\w\-]+)/$', views.prestar, name='prestar'),
	url(r'^reservacion/(?P<idl>[\w\-]+)/$', views.reservacion, name='reservacion'),
	url(r'^ver_mas/(?P<idc>[\w\-]+)/$', views.ver_mas, name='ver_mas'),
	url(r'^reservaciones/$', views.reservaciones, name='reservaciones'),
	url(r'^estadisticas/$', views.estadisticas, name='estadisticas'),
	url(r'^ver_mas_motivacional/$', views.ver_mas_motivacional, name='ver_mas_motivacional'),
	url(r'^ver_mas_general/$', views.ver_mas_general, name='ver_mas_general'),
	url(r'^ver_mas_referencia/$', views.ver_mas_referencia, name='ver_mas_referencia'),
	url(r'^ver_mas_espiritual/$', views.ver_mas_espiritual, name='ver_mas_espiritual'),
	url(r'^confirmar_reservacion/(?P<idl>[\w\-]+)/$', views.confirmar_reservacion, name='confirmar_reservacion'),
]
