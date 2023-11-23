import time
from selenium.webdriver.common.by import By

class Footer:
    def __init__(self, driver):
        self.driver = driver

    def VerifyFooter(self):
        # linkedin
        # linkedIn = self.driver.find_element(By.XPATH, '//a[@href="https://www.linkedin.com/company/mncnowid/jobs/"]')
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", linkedIn)
        # time.sleep(2)
        # linkedIn.click()
        # main_window = self.driver.current_window_handle
        # for handle in self.driver.window_handles:
        #     if handle != main_window:
        #         self.driver.switch_to.window(handle)
        #         break
        # assert "https://id.linkedin.com/company/mncnowid" in self.driver.current_url
        # self.driver.close()
        # self.driver.switch_to.window(main_window)

        # # tiktok
        # linkedIn = self.driver.find_element(By.XPATH, '//a[@href="https://www.tiktok.com/@visionplusid"]')
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", linkedIn)
        # time.sleep(1)
        # linkedIn.click()
        # main_window = self.driver.current_window_handle
        # for handle in self.driver.window_handles:
        #     if handle != main_window:
        #         self.driver.switch_to.window(handle)
        #         break
        # assert "https://www.tiktok.com/@visionplusid" in self.driver.current_url
        # self.driver.close()
        # self.driver.switch_to.window(main_window)

        # # instagram
        # linkedIn = self.driver.find_element(By.XPATH, '//a[@href="https://www.instagram.com/visionplusid/"]')
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", linkedIn)
        # time.sleep(1)
        # linkedIn.click()
        # main_window = self.driver.current_window_handle
        # for handle in self.driver.window_handles:
        #     if handle != main_window:
        #         self.driver.switch_to.window(handle)
        #         break
        # assert "https://www.instagram.com/visionplusid/" in self.driver.current_url
        # self.driver.close()
        # self.driver.switch_to.window(main_window)

        # # youtube
        # linkedIn = self.driver.find_element(By.XPATH, '//a[@href="https://www.youtube.com/channel/UCaXBWtWY6XCWFGMTLHaPHJA"]')
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", linkedIn)
        # time.sleep(1)
        # linkedIn.click()
        # main_window = self.driver.current_window_handle
        # for handle in self.driver.window_handles:
        #     if handle != main_window:
        #         self.driver.switch_to.window(handle)
        #         break
        # assert "https://www.youtube.com/channel/UCaXBWtWY6XCWFGMTLHaPHJA" in self.driver.current_url
        # self.driver.close()
        # self.driver.switch_to.window(main_window)

        footer = self.driver.find_element(By.XPATH, '//p[contains(., "Copyright © 2023 Vision+ Academy. All Rights Reserved")]')
        footer_text = footer.text
        assert footer_text == "Copyright © 2023 Vision+ Academy. All Rights Reserved"
