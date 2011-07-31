import sigurd

class BaseWebConfigBase(sigurd.BaseAppConfig):
    WEBSERVICE_LINK = "http://rambler.com.ua"

    def init_settings(self):
        self.MY_CONSTANT = "MAMBOOO"

    def init_extensions(self):
        self.install_app("web")
        self.install_middleware_class("web.middleware.RegionSelectorMiddleware", prepend=True)
        self.install_context_processor("web.context_processors.add_sigurd_profile")

    def init_urls(self, main_urls):
        self.install_url(main_urls, r'^$', 'web.urls')

class ProdWebConfig(BaseWebConfigBase):
    WEBSERVICE_LINK = "http://yandex.com.ua"

class DevWebConfig(BaseWebConfigBase):
    WEBSERVICE_LINK = "http://google.com.ua"

