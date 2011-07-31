import sigurd

# @TODO: UNIMPLEMENTED CODE FOR DJANGO DASH (FUTURE IDEA)

class Dependencies(sigurd.BaseDependencies):
    EXT_APPS_PATH = "apps/ext/"
    EXT_LIBS_PATH = "ext_libs/"
    EXT_STATIC_PATH = "static/ext/"

    def resolve_apps(self):
        self.resolve_app("admin-tools", version="0.2", config_only=True, config_id="dashboard_only")
        self.resolve_app("admin-tools", version="0.2", config_only=True)
        self.resolve_app("haystack", version="3.1")

    def resolve_libs(self):
        self.resolve_lib("python-twitter")
        self.resolve_lib("whoosh", "0.2")

    def resolve_statics(self):
        self.resolve_static("jquery", version="1.6.1")
        self.resolve_static("fancybox", version="0.1")

