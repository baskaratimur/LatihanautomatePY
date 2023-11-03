import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
# untuk dinamis, kalau element ga ada, dan ada
from selenium.common.exceptions import NoSuchElementException


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def VerifyHomepage(self):
        h1Vision = self.driver.find_element(By.XPATH, '//h1[contains(., "Vision+") and contains(., "Academy")]')
        h1Vision_text = h1Vision.text
        assert "Vision+" in h1Vision_text

        video = self.driver.find_element(By.XPATH, '//source[@type="video/mp4"]')
        # assert video muncul
        assert video is not None

        h2Perks = self.driver.find_element(By.XPATH, ' //h2[contains(., "Perks")]')
        h2Perks_text = h2Perks.text
        assert h2Perks_text == "Perks"

        h3RealLife = self.driver.find_element(By.XPATH, ' //h3[contains(., "Real-life Working Experience")]')
        h3RealLife_text = h3RealLife.text
        assert h3RealLife_text == "Real-life Working Experience"

        h3Learning = self.driver.find_element(By.XPATH, ' //h3[contains(., "Learning Opportunities")]')
        h3Learning_text = h3Learning.text
        assert h3Learning_text == "Learning Opportunities"

        h3Supportive = self.driver.find_element(By.XPATH, ' //h3[contains(., "Supportive Workplace")]')
        h3Supportive_text = h3Supportive.text
        assert h3Supportive_text == "Supportive Workplace"

        h3Daily = self.driver.find_element(By.XPATH, ' //h3[contains(., "Daily Allowance")]')
        h3Daily_text = h3Daily.text
        assert h3Daily_text == "Daily Allowance"

        h2Hirring = self.driver.find_element(By.XPATH, ' //h2[contains(., "Hiring Process")]')
        h2Hirring_text = h2Hirring.text
        assert h2Hirring_text == "Hiring Process"

        h2Intern = self.driver.find_element(By.XPATH, ' //h2[contains(., "Intern Stories")]')
        h2Intern_text = h2Intern.text
        assert h2Intern_text == "Intern Stories"
        
        # ambil gambar buat dihover
        elementGambar = self.driver.find_element(By.XPATH, '//img[@src="https://p-visionplus-academy.s3.ap-southeast-3.amazonaws.com/public/inter/cjm435sh8t9aguej6o1g"]')
        actions = ActionChains(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elementGambar)
        # scroll perlu nunggu 
        time.sleep(2) 
        actions.move_to_element(elementGambar).perform()
        # get namanya
        h4Alya = self.driver.find_element(By.XPATH, ' //h4[contains(., "Alya Vionita Salsabilla")]')
        h4Alya_text = h4Alya.text
        assert h4Alya_text == "Alya Vionita Salsabilla"

    
        main_window = self.driver.current_window_handle
        linkedIn = self.driver.find_element(By.XPATH, '//a[@href="https://www.linkedin.com/company/mncnowid/jobs/"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", linkedIn)
        time.sleep(2)
        linkedIn.click()
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        assert "https://id.linkedin.com/company/mncnowid" in self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(main_window)

        footer = self.driver.find_element(By.XPATH, '//p[contains(., "Copyright © 2023 Vision+ Academy. All Rights Reserved")]')
        footer_text = footer.text
        assert footer_text == "Copyright © 2023 Vision+ Academy. All Rights Reserved"



