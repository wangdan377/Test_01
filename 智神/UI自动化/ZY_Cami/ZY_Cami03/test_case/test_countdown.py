from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner
from test_case import test_beautify
# from test_case.test_beautify import Beautify_Fair
# from .test_beautify import Beautify_Fair
from test_case.test_beautify import Beautify_Fair


class Countdown(object):
    """倒计时"""
    def __init__(self):
        self.pics = Beautify_Fair()  # 是实例化
        self.driver1 = self.pics.devices()
        self.pics.connecting01()

    """def devices(self):
        desired_caps = {'platformName': 'Android',  # 手机系统
                        'deviceName': '7HX0219918017044',
                        'noReset': True,  # 防止每次启动时软件初始化
                        'appPackage': 'com.zhiyun.cama',
                        'appActivity': '.splash.SplashActivity',
                        'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串
                        'resetKeyboard': True}  # 将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        desired_caps['newCommandTimeout'] = 6000
        self.driver.implicitly_wait(15)
        # print('启动app')
        return self.driver"""
    """def countdown00(self):
        pics = Beautify_Fair()  # 是实例化
        self.driver = pics.devices()  # 调用Beautify_Fair类里函数devices()
        pics.connecting01()  # 不连接设备
        return ''"""
    def countdown01(self):
        # driver = self.driver
        # c = Beautify_Fair()
        # c.devices()
        # Beautify_Fair.devices()
        # Beautify_Fair.connecting01()
        # self.couns.devices()
        # self.couns.connecting01()
        # print(self.couns.connecting01())
        driver = self.driver1
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_countdown").click()  # 倒计时
        return '倒计时'

    """def countdown02(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[4]").click()  # 倒计时 off
        time.sleep(2)
        return 'off'
    def countdown03(self):
        driver = self.driver
        self.countdown01()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]").click()  # 3秒
        time.sleep(3)
        # self.pics.beautify_01()
        return '3″'
"""

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
    # print(coun.countdown00())
    print(coun.countdown01())
    # print(coun.countdown02())
    # print(coun.countdown03())
    # print(coun.countdown04())
    # print(coun.countdown05())





