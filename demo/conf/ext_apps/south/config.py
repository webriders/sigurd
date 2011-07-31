import sigurd

class SouthConfig(sigurd.BaseAppConfig):

    def init_extensions(self):
        self.install_app("south")