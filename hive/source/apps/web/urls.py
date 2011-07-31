from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('web.views',
    url(r'^$', 'home', name='home'),
    url(r'^configs/$', 'applications_list', name='applications_list'),
    url(r'^configs/add/$', 'add_app_config', name='add_app_config'),
    url(r'^configs/add/success/$', 'add_app_config_success', name='add_app_config_success'),
    url(r'^configs/(?P<app_slug>[-\w]+)/download/$', 'config_downloader', name='config_downloader'),
    url(r'^configs/(?P<app_slug>[-\w]+)/(?P<config_slug>[-\w]+)/download/$', 'config_downloader', name='config_downloader'),
)
