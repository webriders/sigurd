import sigurd

class AdminToolsConfig(sigurd.AppConfig):

    def get_settings(self, main_settings):
        # TODO!!!!
        ADMIN_TOOLS_MEDIA_URL = self.main_settings.STATIC_URL + 'ext/'
        ADMIN_TOOLS_THEMING_CSS = '../admin_themes/theophilus/css/theme.css'
        ADMIN_TOOLS_MENU = 'conf.ext_apps.admin_tools.menu.Menu'
        ADMIN_TOOLS_INDEX_DASHBOARD = 'conf.ext_apps.admin_tools.dashboard.IndexDashboard'
        return locals()

    def install(self, main_settings):
        self.install_app("admin_tools", prepend=True)
        self.install_app("admin_tools.theming", prepend=True)
        self.install_app("admin_tools.menu", prepend=True)
        self.install_app("admin_tools.dashboard", append=True)

    def get_urls(self, main_urls):
        self.install_urls(r'^admin_tools/', 'admin_tools.urls', prepend=True)

