import self as self
from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner
from test_case import test_beautify
# from test_case.test_beautify import Beautify_Fair
# from .test_beautify import Beautify_Fair
from test_case.test_beautify import Beautify_Fair

# pic = test_beautify.Beautify_Fair()
class Countdown(object):
    """倒计时"""
    def __init__(self):
        pass

        # self.pic = test_beautify.Beautify_Fair()    #实例化beautify
        # self.driver = self.pic.driver  # 启动app
        # pic.devices()   #启动app
        # pic.connecting01()   #连接相机
        # self.pic.devices()  # 启动app
        # self.pic.connecting01()
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
    def connecting01(self):   #不连接相机/不连接设备
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()  # 相机
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()   #点击帮助
        driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
        # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
        time.sleep(5)
        return '不连接固件，直接进入相册'
    def countdown01(self):  #倒计时
        driver = self.driver
        # pic.connecting01()
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
        return '3″'
    def countdown03(self):
        driver = self.driver
        # self.countdown01()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]").click()  # 3秒
        return '5″'
    def countdown04(self):
        driver = self.driver
        self.countdown01()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()  # 5秒
        return '7″'"""
    """def countdown05(self):
        driver = self.driver
        # self.countdown01()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]").click()  # 7秒
        return 'off'"""

if __name__ == '__main__':
    cou = Countdown()
    print(cou.devices())
    print(cou.connecting01())
    print(cou.countdown01())
    # print(cou.countdown02())
    # print(coun.countdown())
    # print(coun.countdown03())
    # print(cou.countdown04())
    # print(coun.countdown05())





