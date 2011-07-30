class Settings(Sigurd.AppSettings):
    # TODO!!!!
    ADMIN_TOOLS_MEDIA_URL = settings.STATIC_URL + 'ext/'
    
    ADMIN_TOOLS_THEMING_CSS = '../admin_themes/theophilus/css/theme.css'
    ADMIN_TOOLS_MENU = 'conf.ext_apps.admin_tools.menu.Menu'
    ADMIN_TOOLS_INDEX_DASHBOARD = 'conf.ext_apps.admin_tools.dashboard.IndexDashboard'

    def install(self):
        self.install_app("admin_tools", prepend_to_top=True)
        self.install_app("admin_tools.theming", prepend_to_top=True)
        self.install_app("admin_tools.menu", prepend_to_top=True)
        self.install_app("admin_tools.dashboard", prepend_to_top=True)

        self.install_urls(r'^admin_tools/', 'admin_tools.urls')