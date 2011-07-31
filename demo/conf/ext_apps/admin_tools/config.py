import sigurd

class AdminToolsConfigBase(sigurd.BaseAppConfig):
    ADMIN_TOOLS_THEMING_CSS = '../admin_themes/web/css/theme.css'
    ADMIN_TOOLS_MENU = 'conf.ext_apps.admin_tools.menu.Menu'
    ADMIN_TOOLS_INDEX_DASHBOARD = 'conf.ext_apps.admin_tools.dashboard.IndexDashboard'

    def __init__(self, main_settings):
        super(AdminToolsConfigBase).__init__(main_settings)
        self.ADMIN_TOOLS_MEDIA_URL = self.main_settings.STATIC_URL + 'ext/'

    def install(self):
        self.install_app("admin_tools", prepend=True)
        self.install_app("admin_tools.theming", prepend=True)
        self.install_app("admin_tools.menu", prepend=True)
        self.install_app("admin_tools.dashboard")

    def get_urls(self, main_urls):
        self.install_urls(r'^admin_tools/', 'admin_tools.urls', prepend=True)