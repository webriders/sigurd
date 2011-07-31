import os
from conf.apps.web.config import ProdWebConfig
from conf.profiles.main import MainProjectConfig

class DevProjectConfig(MainProjectConfig):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DevProjectConfig.PROJECT_ROOT, 'source/db/database.sqlite')
        }
    }

    def install_apps(self):
        self.install_app(ProdWebConfig)

DevProjectConfig().export_settings(globals())

#ACTIVE_PROFILE = DevProjectConfig().export_settings(globals())
#ACTIVE_PROFILE.export_settings(globals())
