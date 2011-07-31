from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# SIGURD, please install app urls
urlpatterns = settings.ACTIVE_SIGURD_PROFILE.install_app_urls(urlpatterns)
# Thanks, dude!