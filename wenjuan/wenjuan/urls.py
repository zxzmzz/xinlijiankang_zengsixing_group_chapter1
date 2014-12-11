from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from app.views import home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wenjuan.views.home', name='home'),
    # url(r'^wenjuan/', include('wenjuan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^q/', include('app.urls')),
    url(r'^$', home),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
