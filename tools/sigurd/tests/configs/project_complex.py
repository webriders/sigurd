import os
import sigurd

class HaystackConfig(sigurd.BaseAppConfig):
    HAYSTACK_SITECONF = 'conf.haystack.fulltext_search'
    HAYSTACK_SEARCH_ENGINE = 'whoosh'

    def init_settings(self):
#        self.HAYSTACK_WHOOSH_PATH = os.path.join(self.get_main_setting("PROJECT_ROOT"), 'search_index')
        self.HAYSTACK_WHOOSH_PATH = os.path.join(self.main_settings.PROJECT_ROOT, 'search_index')

    def init_extensions(self):
        self.install_app("haystack")

class BaseWebConfig(sigurd.BaseAppConfig):
    #app_name = "web"

    WEBSERVICE_LINK = "http://rambler.com.ua"

    def init_settings(self):
        self.MY_CONSTANT = "MAMBOOO"

    def init_extensions(self):
        self.install_app("web")
        self.install_middleware_class("web.middleware.RegionSelectorMiddleware", prepend=True)
        self.install_context_processor("web.context_processors.add_cities")

    def init_urls(self, main_urls):
        self.install_url(main_urls, r'^$', 'web.urls')
        self.install_url(main_urls, r'^profile/$', 'web.urls.profile', prepend=True)


class ProdWebConfig(BaseWebConfig):
    WEBSERVICE_LINK = "http://yandex.com.ua"

class DevWebConfig(BaseWebConfig):
    WEBSERVICE_LINK = "http://google.com.ua"


class TestComplexProjectConfig(sigurd.BaseProjectConfig):
    # Django settings for demo project.

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        # ('Your Name', 'your_email@example.com'),
    )

    MANAGERS = ADMINS

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # On Unix systems, a value of None will cause Django to use the same
    # timezone as the operating system.
    # If running in a Windows environment this must be set to the same as your
    # system time zone.
    TIME_ZONE = 'America/Chicago'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale
    USE_L10N = True

    PROJECT_ROOT = "/home/demo/app/"


    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = ''

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = ''

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in ext_apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = ''

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    # URL prefix for admin static files -- CSS, JavaScript and images.
    # Make sure to use a trailing slash.
    # Examples: "http://foo.com/static/admin/", "/static/admin/".
    ADMIN_MEDIA_PREFIX = '/static/admin/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = '9t@&k%t)rrpl^6f68)(rf-4(k*d8nxmgit3zqdvw6osl-3xl)0'

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    ROOT_URLCONF = 'demo.urls'

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        # 'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
    )

    def install_apps(self):
        self.install_app(HaystackConfig)
        self.install_app("sigurd.tests.configs.project_complex.BaseWebConfig")

class DemoTestComplexProjectConfig(TestComplexProjectConfig):
    DEBUG=True

    def install_apps(self):
        self.install_app("sigurd.tests.configs.project_complex.BaseWebConfig")

class ProdTestComplexProjectConfig(TestComplexProjectConfig):
    DEBUG=False

    def install_apps(self):
        self.install_app(HaystackConfig)
