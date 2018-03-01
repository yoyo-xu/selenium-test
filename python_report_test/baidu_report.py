#---coding:utf-8---
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Baidu(unittest.TestCase):
	"""docstring for Baidu"""
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.implicitly_wait(10)
		self.base_url="http://www.baidu.com/"

	def test_baidu_search(self):
		"""key_words:HTMLTestRunner"""
		driver=self.driver
		driver.get(self.base_url)
		driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
		driver.find_element_by_id("su").click()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	
	testunit=unittest.TestSuite()
	testunit.addTest(Baidu("test_baidu_search"))
	# 按照一定格式获取当前时间
	now=time.strftime("%Y-%m-%d %H_%M_%S")
	# 定义存放路径
	fp=open('./'+now+'result.html','wb')
	# 定义测试报告
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度报告',description=u'用例执行情况:')
	# 运行测试用例
	runner.run(testunit)
	# 关闭测试报告
	fp.close()