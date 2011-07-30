
class Dependencies(object):
    EXT_APPS = "apps/ext/"
    EXT_LIBS = "ext_libs"

    def application_deps(self):
        self.require_app("admin-tools", version="0.2", config_only=True, config_id="dashboard_only")
        self.require_app("admin-tools", version="0.2", config_only=True)
        self.require_app("haystack", version="3.1")

    def lib_deps(self):
        self.require_lib("python-twitter")
        self.require_lib("whoosh", "0.2")
