import sigurd

class CeleryConfig(sigurd.BaseAppConfig):
    app_name = "celery"

    def init_extensions(self):
        self.install_app("celery")

