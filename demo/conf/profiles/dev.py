import os
from conf.apps.web.config import DevWebConfig
from conf.ext_apps.celery.config import CeleryConfig
from conf.ext_apps.debug_toolbar.config import DebugToolbarConfig
from conf.ext_apps.haystack.config import HaystackConfig
from conf.ext_apps.registration.config import RegistrationConfig
from conf.ext_apps.south.config import SouthConfig
from conf.profiles.main import MainProjectConfig

class DevProjectConfig(MainProjectConfig):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(MainProjectConfig.PROJECT_ROOT, 'demo/db/database.sqlite')
        }
    }

    def install_apps(self):
        # custom
        self.install_app(DevWebConfig)

        # external
        self.install_app(HaystackConfig)
        self.install_app(SouthConfig)
        self.install_app("conf.ext_apps.admin_tools.config.AdminToolsConfig")
        self.install_app(DebugToolbarConfig)
        self.install_app(CeleryConfig)
        self.install_app(RegistrationConfig)

DevProjectConfig().export_settings(globals())
