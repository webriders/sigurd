class Settings(Sigurd.AppSettings):
    ENABLED = True

    ACCOUNT_ACTIVATION_DAYS = 7

    def install(self):
        self.install_app("registration")
        self.install_urls(r'^accounts/', 'registration.backends.default.urls')