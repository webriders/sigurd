import sigurd

class BaseWebConfig(sigurd.AppConfig):
    WEBSERVICE_LINK = "http://rambler.com.ua"

    def __init__(self, main_setting):
        super(BaseWebConfig).__init__(main_setting)
        self.MY_CONSTANT = "MAMBOOO"

    def install(self):
        self.install_app("web")
        self.install_middleware("web.middleware.RegionSelectorMiddleware", prepend=True)
        self.install_context_processor("web.context_processors.add_cities")

    def install_urls(self, main_urls):
        self.install_url(main_urls, r'^$', 'web.urls')



class ProdWebConfig(BaseWebConfig):
    WEBSERVICE_LINK = "http://yandex.com.ua"

class DevWebConfig(BaseWebConfig):
    WEBSERVICE_LINK = "http://google.com.ua"

