import unittest
from RepositoryVision.RepoNavbar import Header
from RepositoryVision.RepoHomepage import Homepage
from RepositoryVision.RepoFooter import Footer

class TestVerifyHomepage(unittest.TestCase):
    def test_verify_homepage(self):
        from setup import SetupDriver
        # buat setupnya
        driver = SetupDriver()
        # panggil objek header
        header = Header(driver)

        # panggil objek homepage
        homepage = Homepage(driver)

        footer = Footer(driver)
        driver.get("https://academy.visionplus.id")
        header.VerifyNavbar()
        homepage.VerifyHomepage()
        footer.VerifyFooter()
        print("berhasil diverify homepage")
        self.assertEqual(True, True)


