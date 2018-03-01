# -*- coding: utf-8 -*-
from sel
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LiangshiLoginOut(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://liangshi.gpdi.com:8088/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_liangshi_login_out(self):
        driver = self.driver
        driver.get(self.base_url + "/#!/login")
        driver.find_element_by_xpath("//li[6]/span").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("admin")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("qazWSXedc")
        driver.find_element_by_id("Verification").clear()
        driver.find_element_by_id("Verification").send_keys("wwo8")
        driver.find_element_by_css_selector("p.loginBoxbtn").click()
        driver.find_element_by_id("errTis").click()
        driver.find_element_by_id("Verification").clear()
        driver.find_element_by_id("Verification").send_keys("f52p")
        driver.find_element_by_css_selector("p.loginBoxbtn").click()
        driver.find_element_by_xpath("//li[6]/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
