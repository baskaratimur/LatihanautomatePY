import unittest
from RepositoryVision.RepoNavbar import Header
from setup import SetupDriver
from TestCase.ActionsHomepage import TestVerifyHomepage

class TestClickNavbar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = TestVerifyHomepage.driver

    def test_click_navbar(self):
        header = Header(self.driver)
        header.ClickNavAbout()
        header.ClickNavLife()
        header.ClickNavBatch()
        header.ClickNavFaq()
        print("berhasil diclick navbar")
        self.assertEqual(True, True)

    @classmethod
    def tearDownClass(cls):
        pass
