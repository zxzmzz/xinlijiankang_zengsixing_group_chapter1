from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from app.views import questionnaire

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wenjuan.views.home', name='home'),
    # url(r'^wenjuan/', include('wenjuan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^(\d+)/$', questionnaire),
)
