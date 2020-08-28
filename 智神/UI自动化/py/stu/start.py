"""import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)"""
from appium import webdriver
 
"""global driver


class Test(object):
    def setUp(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '7HX0219918017044'
        desired_caps['appPackage'] = 'com.zhiyun.cama'
        desired_caps['appActivity'] = '.splash.SplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['newCommandTimeout'] = '1232000'
        # desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    t = Test()
    t.setUp()"""

# coding=utf-8

from time import sleep
import time
import random
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

'''desired_caps = {
                'platformName': 'Android',
                'deviceName': '7HX0219918017044',
                'platformVersion': '10',
                'appPackage': 'com.zhiyun.cama',
                'appActivity': '.splash.SplashActivity',
                "noReset": 'true'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)'''
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()
