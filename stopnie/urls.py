from django.conf.urls import url
from stopnie import views

urlpatterns = [
    url(r'^$', views.Stopnie.as_view(), name='stopnie'),
    url(r'^(?P<stopien_id>\d+)/$', views.Stopien_.as_view(), name='stopien'),
    url(r'^(?P<stopien_id>\d+)/add_rejestracja/$', views.Rejestracja.as_view(), name='add_rejestracja'),
    url(r'^(?P<kandydat_id>\d+)/ankieta/$', views.Ankieta.as_view(), name='ankieta')
]
