class Settings(Sigurd.AppSettings):
    ENABLED = False

    def install(self):
        self.install_app("celery")
