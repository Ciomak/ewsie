from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = [
    url(r'^statistica/', include('statistica.urls')),
    url(r'^stopnie/', include('stopnie.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
