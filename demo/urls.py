from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
urlpatterns = settings.ACTIVE_SIGURD_PROFILE.install_app_urls(urlpatterns)
print str(urlpatterns)