from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http.response import HttpResponse
from django.views.static import serve as static_serve
from wiki.compat import include, url
from . import views
from wiki import sites

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots.txt', lambda _: HttpResponse('User-agent: *\nDisallow: /')),
    url(r'^test1/', views.test1, name='wikitest1'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
    ]


urlpatterns += [
    url(r'^notify/', include('django_nyt.urls')),
    url(r'', views.myhome, name='myhome'),
    url(r'^wiki/', include('wiki.urls')),
]

handler500 = 'testproject.views.server_error'
handler404 = 'testproject.views.page_not_found'
