import sigurd

class Settings(sigurd.AppConfig):

    def install(self):
        self.install_app("celery")
