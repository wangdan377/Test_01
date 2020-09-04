#coding=utf-8
import os,time
from appium import webdriver
from time import sleep

"""desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = '7HX0219918017044'
desired_caps['appPackage'] = 'com.huawei.calculator'
desired_caps['appActivity'] = 'com.huawei.calculator.Calculator'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_name("2").click()
driver.find_element_by_name("0").click()
driver.find_element_by_name("1").click()
driver.find_element_by_name("8").click()
driver.quit()   #执行完退出"""
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = '7HX0219918017044'
desired_caps['appPackage'] = 'com.huawei.calculator'
desired_caps['appActivity'] = 'com.huawei.calculator.Calculator'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.find_element_by_id("com.huawei.calculator:id/digit_7").click()
# driver.find_element_by_accessibility_id("乘").click()
# driver.find_element_by_id("com.huawei.calculator:id/digit_7").click()
# driver.find_element_by_accessibility_id("等于").click()
sleep(5)
driver.quit()
# 0123456789ABCDEF
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
# 7HX0219918017044
# desired_caps['appPackage'] = 'com.huawei.calculator'
# desired_caps['appActivity'] = 'com.huawei.calculator.Calculator'
"""
# -*- coding: utf-8 -*-

from appium import webdriver

desired_caps = {
        'platformName': 'Android',
        'deviceName': '7HX0219918017044',
        'platformVersion': '10',
        'appPackage': 'com.huawei.calculator',
        'appActivity': '.calculator.Calculator'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_name('7').click()
driver.find_element_by_name('+').click()
driver.find_element_by_name('8').click()
driver.find_element_by_name('=').click()
# driver.quit()
"""





