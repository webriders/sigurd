import sigurd

class SouthConfig(sigurd.AppConfig):

    def install(self):
        self.install_app("south")