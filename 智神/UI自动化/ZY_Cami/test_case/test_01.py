# conding=utf-8
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
    num+=1