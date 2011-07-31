from unittest import TestCase

from configs.project_complex import TestComplexProjectConfig
from sigurd import BaseProjectConfig

class TestProjectConfig(TestCase):

    def test_export_globals(self):
        project_config = TestComplexProjectConfig()
        globals_dict = globals()
        project_config.export_settings(globals_dict)

        self.assertEquals(globals_dict["TEMPLATE_DIRS"], ())
        self.assertEquals(globals_dict[BaseProjectConfig.ACTIVE_PROFILE_GLOBALS_KEY], project_config)

#        for key in globals_dict.keys():
#            print "%s: %s" % (str(key), str(globals_dict[key]))
#
#    def test_export_globals_set_active_profile(self):
#        project_config = TestComplexProjectConfig()
#        globals_dict = globals()
#        project_config.export_settings(globals_dict)
#        self.assertEquals(globals_dict[BaseProjectConfig.ACTIVE_PROFILE_GLOBALS_KEY], project_config)
