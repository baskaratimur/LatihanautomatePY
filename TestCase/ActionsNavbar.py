import unittest
from RepositoryVision.RepoNavbar import Header

class TestClickNavbar(unittest.TestCase):
    def test_click_navbar(self):
        from setup import SetupDriver
        driver = SetupDriver()
        driver.get("https://academy.visionplus.id")
        header = Header(driver)
        header.ClickNavLife()
        header.ClickNavBatch()
        header.ClickNavFaq()
        print("berhasil diclick navbar")



