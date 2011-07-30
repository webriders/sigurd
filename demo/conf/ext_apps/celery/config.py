import sigurd

class CeleryConfig(sigurd.AppConfig):

    def install(self):
        self.install_app("celery")
