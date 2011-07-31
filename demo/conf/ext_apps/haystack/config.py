import os
import sigurd

class HaystackConfig(sigurd.BaseAppConfig):
    HAYSTACK_SITECONF = 'conf.ext_apps.haystack.fulltext_search'
    HAYSTACK_SEARCH_ENGINE = 'whoosh'

    def init_settings(self):
        self.HAYSTACK_WHOOSH_PATH = os.path.join(self.main_settings.PROJECT_ROOT, 'search_index')

    def init_extensions(self):
        self.install_app("haystack")
