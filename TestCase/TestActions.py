import unittest
from RepositoryVision.RepoNavbar import Header
from setup import SetupDriver
from TestCase.ActionsHomepage import TestVerifyHomepage
import time

class TestCLickActions(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
                cls.driver = TestVerifyHomepage.driver
                
        def test_actions(self):
                # from setup import SetupDriver
                # driver = SetupDriver()
                # header = Header(driver)
                header = Header(self.driver)
                header.ClickNavLife()
                print("berhasil diclick navbar")
                self.assertEqual(True, True)

        @classmethod
        def tearDownClass(cls):
                cls.driver.quit()