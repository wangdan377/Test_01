from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner

desired_caps ={'platformName':'Android',#手机系统
                'deviceName':'7HX0219918017044',
                'noReset':True,#防止每次启动时软件初始化
                'appPackage':'com.zhiyun.cama',
                'appActivity':'.splash.SplashActivity',
                'unicodeKeyboard':True,#使用unicode编码方式发送字符串
                'resetKeyboard':True}#将键盘隐藏起来
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Home\"]/android.widget.ImageView").click()   #进入首页
driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()	  #相机
time.sleep(2)
driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()	 #问号
time.sleep(2)
driver.find_element_by_id("com.zhiyun.cama:id/enter").click()	  #不连设备,直接进入
time.sleep(2)
# driver.find_element_by_id("com.zhiyun.cama:id/iv_beauty").click()    #美颜
# time.sleep(2)
# 获取屏幕的size
size = driver.get_window_size()
# print(size)   #{'width': 1176, 'height': 2206}  首页的宽高
              # {'width': 2328, 'height': 1128}    拍照的宽高

x = driver.get_window_size()["width"]
y = driver.get_window_size()["height"]
# z = driver.swipe(x*0.5,y*0.5,x*0.5,y*0.5,duration=2000)
# s=driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 3 * y, 200)#向上滑动
# time.sleep(2)
time.sleep(2)
# driver.swipe( x*0.15, y*0.3, x*0.15, y*0.8, 200)#向下滑动  x不变  y由小变大  美颜向下滑动
# time.sleep(2)
# driver.tap([(1100,265),(1150,325)],500)
# time.sleep(2)
# driver.swipe( x*0.96, y*0.52, x*0.96, y*0.58, 200)#向下滑动  x不变  y由小变大  拍照-录像，但是会记录上次的结果
# driver.swipe( x*0.96, y*0.52, x*0.96, y*0.46, 200)#向上滑动  x不变  y由大变小
time.sleep(2)
driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()

driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()




# for i in range(5):   for循环
#     driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 5 * y, 200)  # 向上滑动
#     time.sleep(2)
# driver.tap([(500,1000),(500,613)],500)
# time.sleep(2)
# 向左滑动。y轴保持不变，X轴：由大变小
"""def swipe_left(driver,star_x=0.9,stop_x=0.1,duration=2000):
    x1 = int(x*star_x)
    y1 = int(y*0.5)
    x2 = int(x*stop_x)
    y2 = int(y*0.5)
    driver.swipe(x1,y1,x2,y2,duration)
    return swipe_left
print(swipe_left(driver))"""
# 向右滑动。y轴保持不变，X轴：由小变大
"""def swipe_right(driver,star_x=0.1,stop_x=0.9,duration=2000):
    x1 = int(x*star_x)
    y1 = int(y*0.5)
    x2 = int(x*stop_x)
    y2 = int(y*0.5)
    driver.swipe(x1,y1,x2,y2,duration)"""

# 向上滑动。x轴保持不变，y轴：由大变小
"""def swipe_up(driver,star_y=0.9,stop_y=0.1,duration=2000):
    x1 = int(x*0.5)
    y1 = int(y*star_y)
    x2 = int(x*0.5)
    y2 = int(y*stop_y)
    driver.swipe(x1,y1,x2,y2,duration)
    return x1,y1,x2,y2
print(swipe_up(driver))"""
# 向下滑动。x轴保持不变，y轴：由小变大
"""def swipe_down(driver,star_y=0.1,stop_y=0.9,duration=2000):
    x1 = int(x*0.5)
    y1 = int(y*star_y)
    x2 = int(x*0.5)
    y2 = int(y*stop_y)
    driver.swipe(x1,y1,x2,y2,duration)"""


"""if __name__=='__main__':
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    swipe_left(driver)
    swipe_right(driver)
    swipe_up(driver)
    swipe_down(driver)"""