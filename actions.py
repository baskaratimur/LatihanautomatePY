import time
from selenium.webdriver.common.by import By

def close_popups(driver):
    time.sleep(2)
    driver.find_element(By.XPATH,  '//button[@class= "driver-close-btn driver-close-only-btn"]').click()
    driver.find_element(By.XPATH,  "//button[contains(text(),'Nanti Saja')]").click()

def login(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Masuk')]").click()
    driver.find_element(By.NAME, 'username').send_keys('baskaratimur2@gmail.com')
    driver.find_element(By.NAME, 'password').send_keys('@Testing123')
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@class = "mw-ripple-effect btn rounded text-sm relative overflow-hidden w-full btn-filled text-neutral-1000 bg-primary-1 uppercase qa-login-button"]').click()

# Tambahkan fungsi lainnya di sini...
