from unittest import TestCase
from sigurd import utils
from sigurd.tests.configs.project_complex import ProdWebConfig

class TestUtils(TestCase):

    def test_get_class_by_path(self):
        prod_web_config = utils.get_class_by_path("sigurd.tests.configs.project_complex.ProdWebConfig")
        print str(ProdWebConfig)
        print str(prod_web_config)

        self.assertEquals(ProdWebConfig, prod_web_config)

    def test_get_class_by_path_invalid_path(self):
        try:
            prod_web_config = utils.get_class_by_path("sigurd.blabla.project_complex.ProdWebConfig")
            self.fail("ImportError was not called for wrong package pass")
        except ImportError:
            # OK
            pass

    def test_get_class_by_path_invalid_class_name(self):
        try:
            prod_web_config = utils.get_class_by_path("sigurd.tests.configs.project_complex.BlablaProdWebConfig")
            self.fail("AttributeError was not called for wrong class name")
        except AttributeError:
            # OK
            pass
