# coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time, os


class Base(object):
    """driver = None
    desired_caps = {'platformName': 'Android',  # 手机系统
                    'deviceName': '7HX0219918017044',
                    'noReset': True,  # 防止每次启动时软件初始化
                    'appPackage': 'com.zhiyun.cama',
                    'appActivity': '.splash.SplashActivity',
                    'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串
                    'resetKeyboard': True}  # 将键盘隐藏起来

    def __init__(self, appium_driver):
        self.driver = appium_driver"""

    def dev(self):
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
        return ''
    # 重新封装单个元素定位方法
    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面元素未能找到 %s 元素" % (self, loc))

    # 重新封装一组元素定位方法
    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc).click())>=1:
                return self.driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))
            # print(self.driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click())
    def find_element(self):
        driver = self.driver
        try:
            driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()
            time.sleep(5)
            driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()  # 点击帮助
            driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
            # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
            time.sleep(5)
        # except NoSuchElementException as a: #元素不存在，则调用捕获异常处理
        #     Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(a)
        # except NoAlertPresentException as b:   #捕获意外的异常
        #     Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(b)
        except Exception as result:
            # Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(result)
            print('未找到元素')
        else:
            pass  #没有错的情况下执行
        finally:
            pass  #有没有错，都会执行
        return ''
    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            # print(u"%s 页面中未能找到 %s 元素" % (self, loc))
            print(self.driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click())
    # 重新封装输入方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print("%s 页面未能找到 %s 元素" % (self, loc))

    # 重新封装按钮点击方法
    def clickButton(self, loc, find_first=True):
        try:
            if find_first:
                self.find_element(loc)
            self.find_element(loc).click()
        except AttributeError:
            print("%s 页面未能找到 %s 按钮" % (self, loc))

    # savePngName:生成图片的名称
    def savePngName(self, name):
        """
    name：自定义图片的名称
    """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = "Result\\" + day + "\\image\\" + day
        tm = self.saveTime()
        type = ".png"
        if os.path.exists(fp):
            filename = fp + "\\" + tm + "_" + name + type
            print(filename)
            # print "True"
            return filename
        else:
            os.makedirs(fp)
            filename = fp + "\\" + tm + "_" + name + type
            print(filename)
            # print "False"
            return filename

    # 获取系统当前时间
    def saveTime(self):
        """
    返回当前系统时间以括号中（2014-08-29-15_21_55）展示
    """
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    # saveScreenshot:通过图片名称，进行截图保存
    def saveScreenshot(self, name):
        """
    快照截图
    name:图片名称
    """
        # 获取当前路径
        # print os.getcwd()
        image = self.driver.save_screenshot(self.savePngName(name))
        return image
