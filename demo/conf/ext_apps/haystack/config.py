import os
import sigurd

class HaystackConfig(sigurd.AppConfig):
    HAYSTACK_SITECONF = 'conf.haystack.fulltext_search'
    HAYSTACK_SEARCH_ENGINE = 'whoosh'

    def __init__(self, main_settings):
        super(HaystackConfig).__init__(main_settings)
        HAYSTACK_WHOOSH_PATH = os.path.join(main_settings.PROJECT_ROOT, 'search_index')

    def install(self):
        self.install_app("haystack")
