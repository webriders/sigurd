import sigurd

class SouthConfigBase(sigurd.BaseAppConfig):

    def install(self):
        self.install_app("south")