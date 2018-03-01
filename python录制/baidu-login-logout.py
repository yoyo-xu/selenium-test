# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiduLoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu_login_logout(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("aa")
        driver.find_element_by_id("su").click()
        driver.find_element_by_link_text(u"登录").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=FP_UID=94824f130601a137a3655556db32e837 | ]]
        driver.find_element_by_id("TANGRAM__PSP_10__userName").clear()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("xsearchu")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=FP_UID=94824f130601a137a3655556db32e837 | ]]
        driver.find_element_by_id("TANGRAM__PSP_10__password").clear()
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("Xumingming0")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=FP_UID=94824f130601a137a3655556db32e837 | ]]
        driver.find_element_by_id("TANGRAM__PSP_10__verifyCode").clear()
        driver.find_element_by_id("TANGRAM__PSP_10__verifyCode").send_keys(u"学坏")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=FP_UID=94824f130601a137a3655556db32e837 | ]]
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=FP_UID=94824f130601a137a3655556db32e837 | ]]
        driver.find_element_by_link_text(u"退出").click()
    
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
