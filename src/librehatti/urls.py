from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from librehatti.report.views import *

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'librehatti.catalog.views.index'),
    url(r'^catalog/', include('librehatti.catalog.urls')),
    url(r'^useraccounts/', include('useraccounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/','librehatti.report.search.search'),
    url(r'^search_result/','librehatti.report.views.search_result'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
