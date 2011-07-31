from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('web.views',
    url(r'^$', 'home', name='home'),
    url(r'^configs/$', 'applications_list', name='applications_list'),
    url(r'^configs/add/$', 'add_config', name='add_config'),
    url(r'^configs/add/success/$', 'add_config_success', name='add_config_success'),
    url(r'^configs/(?P<app_slug>[-\w]+)/download/$', 'download_config', name='download_config'),
    url(r'^configs/(?P<app_slug>[-\w]+)/(?P<config_slug>[-\w]+)/download/$', 'download_config', name='download_config'),
)
