from django.conf.urls import url
from stopnie import views

urlpatterns = [
	url(r'^$', views.stopnie, name='stopnie'),
	url(r'^(?P<stopien_id>\d+)/$', views.stopien, name='stopien'),
	url(r'^(?P<stopien_id>\d+)/add_rejestracja/$', views.add_rejestracja, name='add_rejestracja'),
	url(r'^(?P<kandydat_id>\d+)/ankieta/$', views.add_ankieta, name='ankieta')
	]