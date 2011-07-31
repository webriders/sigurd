from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('web.views',
    url(r'^$', 'home', name='home'),
)

  