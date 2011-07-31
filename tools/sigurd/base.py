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


