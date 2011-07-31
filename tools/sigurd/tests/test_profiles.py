from unittest import TestCase
from sigurd.tests.configs.project_complex import DemoTestComplexProjectConfig, ProdTestComplexProjectConfig

class TestProjectConfig(TestCase):

    def test_demo_profile(self):
        project_config = DemoTestComplexProjectConfig()
        globals_dict = globals()
        project_config.export_settings(globals_dict)

        self.assertTrue(globals_dict["DEBUG"])
        self.assertTrue("web" in globals_dict["INSTALLED_APPS"])
        self.assertFalse("haystack" in globals_dict["INSTALLED_APPS"])


    def test_prod_profile(self):
        project_config = ProdTestComplexProjectConfig()
        globals_dict = globals()
        project_config.export_settings(globals_dict)

        self.assertFalse(globals_dict["DEBUG"])
        self.assertFalse("web" in globals_dict["INSTALLED_APPS"])
        self.assertTrue("haystack" in globals_dict["INSTALLED_APPS"])

