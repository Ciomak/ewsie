from django.conf.urls import url
from statistica import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^charts/$', views.GenderAgeView.as_view(), name='charts'),
]