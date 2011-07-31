from unittest import TestCase

from configs.project_complex import TestComplexProjectConfig
from sigurd import BaseProjectConfig

class TestProjectConfig(TestCase):

    def test_export_globals(self):
        project_config = TestComplexProjectConfig()
        globals_dict = globals()
        project_config.export_settings(globals_dict)

        self.assertEqual(globals_dict["TEMPLATE_DIRS"], ())
        self.assertEqual(globals_dict[BaseProjectConfig.ACTIVE_PROFILE_GLOBALS_KEY], project_config)

        # check app HAYSTACK
        self.assertTrue("haystack" in globals_dict["INSTALLED_APPS"])

        # check static attrs
        self.assertEqual(globals_dict["HAYSTACK_SITECONF"], "conf.haystack.fulltext_search")
        self.assertEqual(globals_dict["HAYSTACK_SEARCH_ENGINE"], "whoosh")

        # check dynamic attrs
        self.assertEqual(globals_dict["HAYSTACK_WHOOSH_PATH"], "/home/demo/app/search_index")

        # -------------------------------------------------------
        # check app WEB
        self.assertTrue("web" in globals_dict["INSTALLED_APPS"])

        # check static attrs
        self.assertEqual(globals_dict["WEBSERVICE_LINK"], "http://rambler.com.ua")

        # check dynamic attrs
        self.assertEquals(globals_dict["MY_CONSTANT"], "MAMBOOO")

        # check extensions
        self.assertTrue("web.middleware.RegionSelectorMiddleware" in globals_dict["MIDDLEWARE_CLASSES"])
        # check prepend
        self.assertEqual(globals_dict["MIDDLEWARE_CLASSES"][0], "web.middleware.RegionSelectorMiddleware")

        ctxs = globals_dict["TEMPLATE_CONTEXT_PROCESSORS"]
        self.assertTrue("web.context_processors.add_cities" in ctxs)
        # check append
        self.assertEqual(ctxs[len(ctxs) - 1], "web.context_processors.add_cities" )

        
    def test_profiles(self):
        pass
        


    def test_export_globals_set_active_profile(self):
        project_config = TestComplexProjectConfig()
        globals_dict = globals()
        project_config.export_settings(globals_dict)
        self.assertEquals(globals_dict[BaseProjectConfig.ACTIVE_PROFILE_GLOBALS_KEY], project_config)
