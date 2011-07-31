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


#================================================== Application Config =================================================
class AppConfig(Config):
    """
    Django Application config.
    Contains settings and urls.
    """
    def __init__(self, main_settings):
        self.main_settings = main_settings
        self.init_settings()

    def init_settings(self):
        """
        Init your settings.
        Override this method if some of your settings are dependant on main_settings (MEDIA_URL, etc.)
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

    def install_app(self, app_name, prepend=False):
        at = None
        if prepend:
            at = 0
        self.extend_main_list_setting('INSTALLED_APPS', app_name, at)

    def install_middleware_class(self, middleware, prepend=False):
        at = None
        if prepend:
            at = 0
        self.extend_main_list_setting('MIDDLEWARE_CLASSES', middleware, at)

    def install_context_processor(self, context_processor, prepend=False):
        at = None
        if prepend:
            at = 0
        self.extend_main_list_setting('TEMPLATE_CONTEXT_PROCESSORS', context_processor, at)

    def install_settings(self):
        dict = self.get_settings_dict()
        for key, value in dict.itervalues():
            self.set_main_setting(key, value)

    def install(self):
        """
        Install all app settings into the main_settings.
        Override this method if you want to add middlewares, context_processors, etc.
        Don't forget to call self.install_settings() if you want to add your custom app conf settings
        """
        self.install_settings()

    def get_urls(self):
        pass # TODO


#==================================================== Project Config ===================================================
class GlobalProjectConfig(Config):
    def __init__(self):
        from django.conf import global_settings
        for key in dir(global_settings):
            if self.is_setting(key):
                setattr(self, key, getattr(global_settings, key))


class BaseProjectConfig(GlobalProjectConfig):
    def __init__(self):
        custom_settings = self.get_settings_dict()
        super(BaseProjectConfig, self).__init__()
        for key, value in custom_settings.iteritems():
            setattr(self, key, value)

    def get_urls(self):
        pass # TODO