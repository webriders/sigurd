from unittest import TestCase
from django.conf.urls.defaults import patterns, include, url
from sigurd.tests.configs.project_complex import TestComplexProjectConfig

class TestUrls(TestCase):

    def test_urls_installation(self):
        project_config = TestComplexProjectConfig()
        urlpatterns = patterns('',
            url(r'^$', 'demo.views.home', name='home'),
            url(r'^demo/', include('demo.foo.urls'))
        )
        project_config.export_settings({})
        project_config.install_app_urls(urlpatterns)

        # prepend
        self.assertEquals(str(urlpatterns[0]), str(url(r'^profile/$', include('web.urls.profile'))))
        # append
        self.assertEquals(str(urlpatterns[len(urlpatterns)-1]), str(url(r'^$', include('web.urls'))))
