class Settings(Sigurd.AppSettings):

    def settings(self, global_settings):
        HAYSTACK_SITECONF = 'conf.haystack.fulltext_search'
        HAYSTACK_SEARCH_ENGINE = 'whoosh'

        # TODO!!!!!!!!
        # HAYSTACK_WHOOSH_PATH = os.path.join(main_settings.PROJECT_ROOT, 'search_index')
        HAYSTACK_WHOOSH_PATH = self.path_from_project_root('search_index')

    def install(self):
        self.install_app("haystack")
