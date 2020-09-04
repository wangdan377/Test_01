from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner
from test_case import test_beautify

class Countdown(object):
    def __init__(self):
        self.pic = test_beautify.Beautify_Fair

    def devices(self):
        desired_caps ={'platformName':'Android',#手机系统
                        'deviceName':'7HX0219918017044',
                        'noReset':True,#防止每次启动时软件初始化
                        'appPackage':'com.zhiyun.cama',
                        'appActivity':'.splash.SplashActivity',
                        'unicodeKeyboard':True,#使用unicode编码方式发送字符串
                        'resetKeyboard':True}#将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return '启动'
    """def connecting01(self):   #不连接相机/不连接设备
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()  # 相机
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()   #点击帮助
        driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
        # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
        time.sleep(5)
        return '不连接固件，直接进入相册'"""
    def countdown01(self):
        driver = self.driver
        self.pic.connecting01(self)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_countdown").click()  # 倒计时
        return '点击倒计时'

    """def countdown(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_countdown").click()  # 倒计时
        return '点击倒计时'"""

    """def countdown02(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[4]").click()  # 倒计时 off
        time.sleep(2)
        return '3″'"""
    """def countdown03(self):
        driver = self.driver
        self.countdown01()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]").click()  # 3秒
        return '5″'"""
    def countdown04(self):
        driver = self.driver
        self.countdown01()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()  # 5秒
        return '7″'
    # def countdown05(self):
    #     driver = self.driver
    #     self.countdown01()
    #     time.sleep(3)
    #     driver.find_element_by_xpath(
    #         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]").click()  # 7秒
    #     return 'off'

if __name__ == '__main__':
    coun = Countdown()
    print(coun.devices())
    # print(coun.connecting01())
    print(coun.countdown01())
    # print(coun.countdown02())
    # print(coun.countdown())
    # print(coun.countdown03())
    print(coun.countdown04())
    # print(coun.countdown05())





