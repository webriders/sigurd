from conf.apps.web.config import DevWebConfig
from conf.ext_apps.celery.config import CeleryConfig
from conf.ext_apps.debug_toolbar.config import DebugToolbarConfig
from conf.ext_apps.haystack.config import HaystackConfig
from conf.ext_apps.registration.config import RegistrationConfig
from conf.ext_apps.south.config import SouthConfig
from conf.profiles.main import MainProjectConfig

class ProdProjectConfig(MainProjectConfig):
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

    def install_apps(self):
        # custom
        self.install_app(DevWebConfig)

        # external
        self.install_app(HaystackConfig)
        self.install_app(SouthConfig)
        self.install_app("conf.ext_apps.admin_tools.config.AdminToolsConfig")
#        self.install_app(DebugToolbarConfig)
        self.install_app(CeleryConfig)
        self.install_app(RegistrationConfig)