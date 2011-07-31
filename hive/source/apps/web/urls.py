from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('web.views',
    url(r'^$', 'home', name='home'),
    url(r'^applications/$', 'applications_list', name='applications_list'),
    url(r'^applications/config/add/$', 'add_app_config', name='add_app_config'),
    url(r'^applications/config/add/success/$', 'add_app_config_success', name='add_app_config_success'),
    url(r'^config/(?P<config_id>\d+)/get/$', 'config_downloader', name='config_downloader'),
)
