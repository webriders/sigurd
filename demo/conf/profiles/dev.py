import os
from conf.apps.web.config import DevWebConfig
from conf.profiles.main import MainProjectConfig

class DevProjectConfig(MainProjectConfig):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(MainProjectConfig.PROJECT_ROOT, 'source/db/database.sqlite')
        }
    }

    def install_apps(self):
        self.install_app(DevWebConfig)

DevProjectConfig().export_settings(globals())
