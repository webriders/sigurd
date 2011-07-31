from __future__ import print_function

import inspect
from sigurd import utils
from sigurd.exceptions import ConfigurationError


class Config(object):
    """
    Abstract Config for Django App/Project.
    """

    def get_settings_dict(self):
        """
        Return all self attributes that are UPPERCASE and not starts with '_'
        """
        data = {}
        for key in dir(self):
            value = getattr(self, key)
            if self.is_setting(key):
                data[key] = value
        return data

    def is_setting(self, key):
        """
        Check if key is setting.
        Setting should be UPPERCASE and not starts with '_'
        """
        return key.isupper() and key[0] != '_'

    def export_settings(self, globals):
        """
        Export all settings to some globals dict (it may be some module globals(), or some function locals(), etc.)
        """
        globals.update(self.get_settings_dict())


#================================================== Application Config =================================================
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
         - ets.
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

    def inject(self):
        self.init_settings()
        self.init_extensions()
        dict = self.get_settings_dict()
        for key, value in dict.items():
            self.set_main_setting(key, value)

    def get_urls(self):
        pass # TODO

    def install_url(self, main_urls, url_regexp_pattern, path_to_urls):
        pass


#==================================================== Project Config ===================================================
class GlobalProjectConfig(Config):
    def __init__(self):
        from django.conf import global_settings

        for key in dir(global_settings):
            if self.is_setting(key):
                setattr(self, key, getattr(global_settings, key))


class BaseProjectConfig(GlobalProjectConfig):
    ACTIVE_PROFILE_GLOBALS_KEY = "ACTIVE_PROFILE"

    def __init__(self):
        custom_settings = self.get_settings_dict()
        super(BaseProjectConfig, self).__init__()
        for key, value in custom_settings.iteritems():
            setattr(self, key, value)

    def install_apps(self):
        """
        Override this method in your config to install list of apps, using self.install_app(app_config).
        This method is basis for profiles.

        You can make several similar configs with different list of apps installed in this method.
        This can be used as profiles.
        """
        pass

    def install_app_urls(self, urlpatterns):
        """
        Install app urls to given URL patterns.
        Used to update project URL patterns.
        """
        pass

    def install_app(self, app_config):
        """
        Installs application config.
        app_config can be class or string with python path to class.
        """

        if inspect.isclass(app_config):
            pass
        elif isinstance(app_config, basestring):
            try:
                app_config = utils.get_class_by_path(app_config)
            except (ImportError, AttributeError), e:
                raise ConfigurationError(
                    "Project config[%s] : Cannot install application config [%s] because of error: %s " % (
                        self.__class__.__name__, str(app_config), str(e)))
        else:
            raise ConfigurationError("Project config[%s] : Cannot install application config, unsupported type [%s]" % (
                self.__class__.__name__, str(app_config)))

        app = app_config(self)
        print("[%s] processing: " % (app.__class__.__name__))
        app.inject()
        print(" = done: %s \n" % (app.__class__.__name__))

    def export_settings(self, globals):
        """
        Installs active profile into globals scope.
        Used to get active profile from conf.settings anythere in django code.
        Example usage: <project_root>.urls.py - to install apps urls.
        """
        print("---------------------------------------")
        print("[SIGURD] Starting project configuration")
        print("---------------------------------------\n")
        self.install_apps()
        super(BaseProjectConfig, self).export_settings(globals)
        globals[self.ACTIVE_PROFILE_GLOBALS_KEY] = self
        print("-- [SIGURD] Finished configuration --")
        print("---------------------------------------\n")
