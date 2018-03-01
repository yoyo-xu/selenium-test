# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiudNews(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baiud_news(self):
        driver = self.driver
        driver.get(self.base_url + "/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baidutop10&wd=%E7%A6%BE%E8%8A%B1%E9%9B%80%E5%8D%87%E7%BA%A7%E4%B8%BA%E6%9E%81%E5%8D%B1&oq=%25E7%25A6%25BE%25E8%258A%25B1%25E9%259B%2580%25E5%258D%2587%25E7%25BA%25A7%25E4%25B8%25BA%25E6%259E%2581%25E5%258D%25B1&rsv_pq=d9906f20000157c7&rsv_t=b4099llRqdNhshYg4sjG70FsYj3uV8lYKbLGnmJwFi5ku0UajSejTh%2FXBLlb39OW0A&rqlang=cn&rsv_enter=0")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("")
        driver.find_element_by_id("su").click()
        driver.find_element_by_id("kw").click()
        driver.find_element_by_link_text(u"新闻").click()
        driver.find_element_by_link_text(u"全球税负大比拼：20多国税负超50% 减税成趋势").click()
    
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
