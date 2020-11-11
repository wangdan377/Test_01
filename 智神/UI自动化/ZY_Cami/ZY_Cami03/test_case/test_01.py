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

#self指的是类实例对象本身，并不是类本身
"""class Person:
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
print(p)"""
"""class Test:
    def prt(self):    #self代表的是类的实例，而self.__class__则指向类
        print(self)
        print(self.__class__)
t = Test()
t.prt()"""
"""class Parent():   #继承时，传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例
    def pprt(self):
        print(self)
class Child(Parent):
    def cprt(self):
        print(self)
c = Child()
c.cprt()
c.pprt()
p = Parent()
p.pprt()
"""
"""class A:
    def a(self):
        self.b = 1
        print(2)

    def c(self):
        # self.a()   #调用上a的函数,第一种方法
        A.a(self)   #调用上a的函数,第二种方法
        d = 2+self.b
        print(d)
        return ''
s =A()
s.c()"""

"""import logging,os
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename=os.path.dirname(os.path.dirname(__file__))+'new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )"""
import os
# from common.loged import Logger
# # log = Logger('D:\ZY_Cami03\logs\\error.log',level='debug')
# try:
#     a = 123
#     print(a[0])
# except Exception as e:
#     Logger('D:\ZY_Cami\\ZY_Cami03\\logs\\error.log', level='error').logger.error(e)
    # Logger('all.log', level='debug')
    # logger.critical('严重')
    # log.logger.debug('debug')
    # log.logger.debug(e)
    # log.logger.info(e)
    # log.logger.warning(e)
    # log.logger.error(e)
    # log.logger.critical(e)

"""import math


def square(x):
    if int(x) is 0:
        raise ValueError('Input argument cannot be zero')
    if int(x) < 0:
        raise TypeError('Input argument must be positive integer')

    return math.pow(int(x), 2)

square(1)
"""
#log
"""from common.loged import Logger
log = Logger('D:\ZY_Cami03\logs\\error.log',level='debug')
try:
    a=123
    print(a[1])
except Exception as e:
    # Logger('D:\ZY_Cami03\logs\\error.log',level='debug')
    log.logger.critical(e)
finally:
    print('123123')
"""





