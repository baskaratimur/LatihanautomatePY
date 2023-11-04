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

        faq1 = self.driver.find_element(By.XPATH, '//button[contains(., "What is Vision+?")]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq1)
        faq1_text = faq1.text
        assert faq1_text == "What is Vision+?"
        time.sleep(1)

        faq2 = self.driver.find_element(By.XPATH, '//button[contains(., "What are the requirements for the Vision+ Academy program?")]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq2)
        faq2_text = faq2.text
        assert faq2_text == "What are the requirements for the Vision+ Academy program?"
        faq2.click()
        time.sleep(1)
       
        faq3 = self.driver.find_element(By.XPATH, '//button[contains(., "Who can join the Vision+ Academy program?")]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq3)
        faq3_text = faq3.text
        assert faq3_text == "Who can join the Vision+ Academy program?"
        faq3.click()
        time.sleep(1)
       
        faq4 = self.driver.find_element(By.XPATH, '//button[contains(., "Is the Vision+ Academy program implemented by WFH or WFO?")]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq4)
        faq4_text = faq4.text
        assert faq4_text == "Is the Vision+ Academy program implemented by WFH or WFO?"
        faq4.click()
        time.sleep(1)

        faq5 = self.driver.find_element(By.XPATH, '//button[contains(., "What are the fields that the students can choose in the Vision+ Academy program?")]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq5)
        faq5_text = faq5.text
        assert faq5_text == "What are the fields that the students can choose in the Vision+ Academy program?"
        faq5.click()
        time.sleep(1)



