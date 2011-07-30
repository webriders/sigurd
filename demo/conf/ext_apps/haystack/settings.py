class HaystackConfig(sigurd.AppConfig):

    def get_settings(self, main_settings):
        HAYSTACK_SITECONF = 'conf.haystack.fulltext_search'
        HAYSTACK_SEARCH_ENGINE = 'whoosh'
        # TODO!!!!!!!!
        # HAYSTACK_WHOOSH_PATH = os.path.join(main_settings.PROJECT_ROOT, 'search_index')
        HAYSTACK_WHOOSH_PATH = self.path_from_project_root('search_index')
        return locals()

    def install(self, main_settings):
        self.install_app("haystack")
