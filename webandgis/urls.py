from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'webandgis.views.home', name='home'),
    # url(r'^webandgis/', include('webandgis.foo.urls')),

    url(r'^layers/', include('layers.urls', namespace='layers')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
