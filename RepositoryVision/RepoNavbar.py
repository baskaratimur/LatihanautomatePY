import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Header:
     def __init__(self, driver):
          self.driver = driver

     def ClickNavAbout(self):
          self.driver.find_element(By.XPATH, '//button[contains(text(), "About") and @class="underline underline-offset-8 decoration-[#00CEBB] text-white text-base font-normal flex items-center gap-2"]').click()
          time.sleep(1)

     
     def ClickNavLife(self):
           self.driver.find_element(By.XPATH, "//button[contains(text(), 'Life at Vision+')]").click()

     
     def ClickNavBatch(self):
          self.driver.find_element(By.XPATH, "//button[contains(text(), 'Batch Openings')]").click()


     def ClickNavFaq(self):
          self.driver.find_element(By.XPATH, "//button[contains(text(), 'FAQ')]").click()
  
     def PerformAbout(self):
          hoverAbout = self.driver.find_element(By.XPATH, '//button[contains(text(), "About") and @class="underline underline-offset-8 decoration-[#00CEBB] text-white text-base font-normal flex items-center gap-2"]')
          actions = ActionChains(self.driver)
          actions.move_to_element(hoverAbout).perform()
          time.sleep(2)

     def VerifyNavbar(self):
          navAbout = self.driver.find_element(By.XPATH, "//button[contains(text(), 'About')]")
          navAbout_text = navAbout.text
          assert navAbout_text == "About"

          navLife = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Life at Vision+')]")
          navLife_text = navLife.text
          assert navLife_text == "Life at Vision+"

          navBatch = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Batch Openings')]")
          navBatch_text = navBatch.text
          assert navBatch_text == "Batch Openings"
          
          navFaq = self.driver.find_element(By.XPATH, "//button[contains(text(), 'FAQ')]")
          navFaq_text = navFaq.text
          assert navFaq_text == "FAQ"