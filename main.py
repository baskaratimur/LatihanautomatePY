from setup import setup_driver
from actions import close_popups, login
import time


driver = setup_driver()
driver.get("https://jamtangan.com")
close_popups(driver)
login(driver)
time.sleep(1)
driver.find_element(By.XPATH, '//button[@class = "mw-ripple-effect btn rounded text-sm relative overflow-hidden w-full btn-filled text-neutral-1000 bg-primary-1 uppercase qa-login-button"]').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 1600);")

# time.sleep(3)
time.sleep(1)
driver.find_element(By.XPATH, '//img[@alt="Citizen Chronograph AI5001-81L Blue Dial Stainless Steel Strap"]').click()
driver.find_element(By.XPATH, "//button[contains(text(), '+ ')]").click()
driver.find_element(By.XPATH, '//button[contains(text(), "LIHAT KERANJANG")]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[contains(text(), "Lanjutkan")]').click()
driver.find_element(By.XPATH, "//div[contains(text(), 'Pilih Pengiriman')]").click()
driver.find_element(By.XPATH, "//div[contains(text(), 'JNE')]").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Pilih Pembayaran')]").click()
driver.find_element(By.XPATH, "//p[contains(text(), 'Virtual Account')]").click()


