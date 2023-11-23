import unittest
from RepositoryVision.RepoNavbar import Header
from RepositoryVision.RepoHomepage import Homepage
from RepositoryVision.RepoFooter import Footer
from setup import SetupDriver

class TestVerifyHomepage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.setup_driver = SetupDriver()
        cls.driver = cls.setup_driver.driver

    def test_verify_homepage(self):
        # panggil objek repo
        header = Header(self.driver)
        homepage = Homepage(self.driver)
        footer = Footer(self.driver)

        self.driver.get("https://academy.visionplus.id")
        header.VerifyNavbar()
        homepage.VerifyHomepage()
        footer.VerifyFooter()
        print("berhasil diverify homepage")
        self.assertEqual(True, True)

    @classmethod
    def tearDownClass(cls):
        pass
