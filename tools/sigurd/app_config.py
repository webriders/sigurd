from __future__ import print_function

from sigurd.base import Config
from django.conf.urls.defaults import include, url

class BaseAppConfig(Config):
    """
    Django Application config.
    Contains settings and urls.
    """
    MIDDLEWARE_CLASSES_KEY = 'MIDDLEWARE_CLASSES'
    CONTEXT_PROCESSORS_KEY = 'TEMPLATE_CONTEXT_PROCESSORS'
    INSTALLED_APPS_KEY = 'INSTALLED_APPS'

    def __init__(self, main_settings):
        self.main_settings = main_settings

    def init_settings(self):
        """
        Init your settings.
        Override this method if some of your settings are dependant on main_settings (MEDIA_URL, etc.)
        """
        pass

    def init_extensions(self):
        """
        Override this method to install your custom django extensions.
         - app
         - middleware;
         - context processors;
         - etc.
        """
        pass

    def init_urls(self, urlpatterns):
        """
        Override this method to install your custom application URL.
        You can do this using self.install_url()
        """
        pass

    def get_main_settings(self):
        return self.main_settings

    def get_main_setting(self, key):
        return getattr(self.main_settings, key)

    def set_main_setting(self, key, value):
        return setattr(self.main_settings, key, value)

    def extend_main_list_setting(self, key, value, at=None):
        """
        Modify list settings
        """
        setting = self.get_main_setting(key)
        if not isinstance(setting, (list, tuple)):
            raise Exception('Trying to extend list setting which not is a list/tuple!')
        if isinstance(setting, list):
            value = [value]
        elif isinstance(setting, tuple):
            value = (value,)
        if at is None:
            setting += value
        else:
            setting = setting[:at] + value + setting[at:]
        self.set_main_setting(key, setting)

    def install_app(self, app_name=None, prepend=False):
        """
        Add app_name to the INSTALLED_APPS
        If app_name is not specified - it tries to find self.app_name
        """
        if not app_name:
            app_name = getattr(self, 'app_name')

        if not app_name:
            return None

        at = None
        if prepend:
            at = 0
        self.extend_main_list_setting(self.INSTALLED_APPS_KEY, app_name, at)
        print(" + app: '%s'" % app_name)

    def install_middleware_class(self, middleware, prepend=False):
        at = None
        if prepend:
            at = 0
        self.extend_main_list_setting(self.MIDDLEWARE_CLASSES_KEY, middleware, at)
        print(" + middleware: '%s'" % middleware)

    def install_context_processor(self, context_processor, prepend=False):
        at = None
        if prepend:
            at = 0
        self.extend_main_list_setting(self.CONTEXT_PROCESSORS_KEY, context_processor, at)
        print(" + context processor: '%s'" % context_processor)

    def install_url(self, urlpatterns, url_regexp_pattern, path_to_urls, prepend=False):
        pattern = url(url_regexp_pattern, include(path_to_urls))
        if prepend:
            urlpatterns.insert(0, pattern)
        else:
            urlpatterns.append(pattern)

    def _inject_settings(self):
        """
        Used by project config to build all django settings
        """
        self.init_settings()
        self.init_extensions()

        dict = self.get_settings_dict()
        for key, value in dict.items():
            self.set_main_setting(key, value)

