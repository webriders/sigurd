class Settings(Sigurd.AppSettings):
    WEBSERVICE_LINK = "http://google.com.ua"
    MY_CONSTANT = "MAMBOOO"

    def install(self, setting):
        self.install_app("web")

        self.install_urls(r'^$', 'web.urls')

        self.install_middleware("web.middleware.RegionSelectorMiddleware", prepend_to_top=True)

        self.install_context_processor("web.context_processors.add_cities")