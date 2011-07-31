from __future__ import print_function

import inspect
from django.conf.urls.defaults import patterns
from sigurd.app_config import BaseAppConfig
from sigurd.base import Config
from sigurd import utils
from sigurd.exceptions import ConfigurationError


class GlobalProjectConfig(Config):
    def __init__(self):
        from django.conf import global_settings

        for key in dir(global_settings):
            if self.is_setting(key):
                setattr(self, key, getattr(global_settings, key))


class BaseProjectConfig(GlobalProjectConfig):
    _ACTIVE_PROFILE_SETTING_NAME = "active_profile"

    def __init__(self):
        self.app_configs = []
        # Backup custom settings (because they will be overridden by globals)
        custom_settings = self.get_settings_dict()
        super(BaseProjectConfig, self).__init__()
        # Restore custom settings
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

    def install_app_urls(self, urlpatterns=None):
        """
        Install app urls to given URL patterns.
        Used to update project URL patterns.
        """
        if not urlpatterns:
            urlpatterns = patterns('')

        for app in self.app_configs:
            app.init_urls(urlpatterns)

        return urlpatterns

    def install_app(self, app_config):
        """
        Installs application config.
        app_config can be class or string with python path to class.
        """
        if isinstance(app_config, basestring):
            try:
                app_config = utils.get_class_by_path(app_config)
            except (ImportError, AttributeError), e:
                raise ConfigurationError(
                    "Project config[%s]: Cannot install application config [%s] because of error: %s " % (
                        self.__class__.__name__, str(app_config), str(e)))
        elif not inspect.isclass(app_config):
            raise ConfigurationError("Project config[%s]: Cannot install application config, unsupported type [%s]" % (
                self.__class__.__name__, str(app_config)))

        if not issubclass(app_config, BaseAppConfig):
            raise ConfigurationError("Project config[%s]: error in [%s], application config must be subclass of %s" % (
                self.__class__.__name__, str(app_config), BaseAppConfig.__name__))

        app = app_config(self)

        print("[%s] processing: " % (app.__class__.__name__))
        app._inject_settings()
        self.app_configs.append(app)
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
        globals.update(self.get_settings_dict())
        globals[self._ACTIVE_PROFILE_SETTING_NAME] = self
        print("-- [SIGURD] Finished configuration --")
        print("---------------------------------------\n")