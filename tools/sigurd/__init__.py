class AppConfig(object):
    def __init__(self, main_settings):
        self.main_settings = main_settings

    def get_settings(self):
        data = {}
        for key in dir(self):
            value = getattr(self, key)
            if self.is_setting(key):
                data[key] = value
        return data

    def is_setting(self, key):
        return key.isupper() and key[0] != '_'

    def insert_list_setting(self, key, value, at=-1):
        self.xxx
