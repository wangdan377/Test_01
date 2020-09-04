"""# conding=utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By

server = 'http://localhost:4723/wd/hub'
desired_caps = {'platformName':'Android',#手机系统
                'deviceName':'AIOJJZ8SV4HMVKS8',
                'noReset':True,#防止每次启动时软件初始化
                'appPackage':'com..xhs',
                'appActivity':'.activity.SplashActivity',
                'unicodeKeyboard':True,#使用unicode编码方式发送字符串
                'resetKeyboard':True}#将键盘隐藏起来
driver = webdriver.Remote(server,desired_caps)
time.sleep(5)
driver.find_element_by_id('com..xhs:id/a0_').click()
chaxun = input('请输入要搜索的内容：')
driver.find_element_by_id('com..xhs:id/aqz').send_keys(u'%s'%chaxun)
# print(chaxun)
driver.find_element_by_id('com..xhs:id/ar2').click()
time.sleep(3)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
num = 0
while num<100:
    driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)#向上滑动
    time.sleep(2)
    driver.tap([(30,441),(335,513)],500)
    time.sleep(2)
    driver.tap([(32,66),(84,118)],500)
    time.sleep(2)
    driver.tap([(385,630),(690,710)],500)
    time.sleep(2)
    driver.tap([(32,66),(84,118)],500)
    time.sleep(5)
    num+=1"""



"""def sum():   #for 循环用函数
    sum = 0
    for n in range(1,5):
        sum = sum + n
    return sum
print(sum())

sum = 0     #for 循环不用函数
for n in range(1,5):
    sum = sum + n
print(sum)"""




"""def beautify_04(self):  # 取消美颜
    driver = self.driver
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]").click()  # 自动美颜 无进度条
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()  # 取消美颜


def beautify_05(self):  # 瘦脸
    driver = self.driver
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]").click()  # 瘦脸
    return ''


def beautify_06(self):  # 磨皮
    driver = self.driver
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()  # 磨皮
    return ''


def beautify_07(self):  # 美白
    driver = self.driver
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]").click()  # 美白
    return ''


def slide(self):
    driver = self.driver
    pass


def beautify_08(self):  # 眼睛放大
    driver = self.driver
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]").click()  # 眼睛放大
    return ''


def beautify_09(self):  # 光照
    driver = self.driver
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()  # 光照
    return ''


def beautify_010(self):  # 红润
    driver = self.driver
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]").click()  # 红润
    return ''"""


class Person:
    def __init__(myname,name):   #self指的是类实例对象本身，并不是类本身
        myname.name = name
    def sayhello(myname):
        print('my name is:',myname.name)
        return ''
p = Person('HELLOW')
print(p.sayhello())

class Preson:
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print('my name is:',self.name)
p = Person('Bill')
print(p)
