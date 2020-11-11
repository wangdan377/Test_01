from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner
from test_case import test_beautify
# from test_case.test_beautify import Beautify_Fair
# from .test_beautify import Beautify_Fair
from test_case01.test_beautify01 import Beautify_Fair


class Countdown(Beautify_Fair):
    """倒计时"""
    def __init__(self):
        Beautify_Fair.__init__(self)
        self.devices()
        self.connecting01()

    def countdown01(self):

        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_countdown").click()  # 倒计时
        return '倒计时'

    def countdown02(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[4]").click()  # 倒计时 off
        time.sleep(2)
        return 'off'
    def countdown03(self):
        driver = self.driver
        print(coun.countdown01())
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]").click()  # 3秒
        time.sleep(3)
        print(coun.countdown01())
        print(coun.countdown02())
        return '3″'


    """def countdown04(self):
        driver = self.driver
        self.countdown01()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()  # 5秒
        # self.countdown01()
        # self.pics.beautify_01()
        return '5″'"""
    # def countdown05(self):
    #     driver = self.driver
    #     self.countdown01()
    #     time.sleep(3)
    #     driver.find_element_by_xpath(
    #         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]").click()  # 7秒
    #     return 'off'

if __name__ == '__main__':
    coun = Countdown()
    # print(coun.devices())
    # print(coun.connecting01())
    print(coun.countdown01())
    print(coun.countdown02())
    print(coun.countdown03())
    # print(coun.countdown04())
    # print(coun.countdown05())





