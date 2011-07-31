
import sigurd

class AdminToolsConfig(sigurd.BaseAppConfig):
    ADMIN_TOOLS_THEMING_CSS = '../admin_themes/web/css/theme.css'
    ADMIN_TOOLS_MENU = 'conf.ext_apps.admin_tools.menu.Menu'
    ADMIN_TOOLS_INDEX_DASHBOARD = 'conf.ext_apps.admin_tools.dashboard.IndexDashboard'

    def init_settings(self):
        self.ADMIN_TOOLS_MEDIA_URL = self.main_settings.STATIC_URL + 'ext/'

    def init_extensions(self):
        self.install_app("admin_tools", prepend=True)
        self.install_app("admin_tools.theming", prepend=True)
        self.install_app("admin_tools.menu", prepend=True)
        self.install_app("admin_tools.dashboard", prepend=True)

    def init_urls(self, urlpatterns):
        self.install_url(urlpatterns, r'^admin_tools/', 'admin_tools.urls', prepend=True)