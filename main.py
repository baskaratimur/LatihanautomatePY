from setup import SetupDriver
from RepositoryVision.RepoNavbar import Header
from RepositoryVision.RepohHomepage import Homepage
import time

# buat setupnya
driver = SetupDriver()
# panggil objek header
header = Header(driver)

# panggil objek homepage
homepage = Homepage(driver)
driver.get("https://academy.visionplus.id")
header.VerifyNavbar()
homepage.VerifyHomepage()
print("berhasil diverify")




