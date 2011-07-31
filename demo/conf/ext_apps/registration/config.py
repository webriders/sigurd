import sigurd

class RegistrationConfig(sigurd.BaseAppConfig):
    ACCOUNT_ACTIVATION_DAYS = 7

    def init_settings(self):
        self.install_app("registration")

    def init_urls(self, urlpatterns):
        self.install_url(urlpatterns, r'^accounts/', 'registration.backends.default.urls')