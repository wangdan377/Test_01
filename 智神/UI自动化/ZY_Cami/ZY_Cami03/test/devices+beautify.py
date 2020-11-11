from appium import webdriver
import time
from test.devices import devic
from test.beautify import connect

class con(object):
    def __init__(self):
        self.dev = devic()
        self.driver = self.devices01()
        self.beau = connect()

    """def beautify_01(self):     #美颜
        driver = self.drivers
        self.dev.devices01()
        self.beau.connecting01()
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_beauty").click()     #美颜
        time.sleep(2)
        # driver.find_element_by_id("com.zhiyun.cama:id/sb_roll").click()     #进度条	[533,150][732,1066]     199  916
        # driver.tap([(1180,540)])  #点击空白区域
        # driver.tap([(632, 1022)])   #横坐标632  #纵坐标1022
        return '点击美颜按钮'"""
# if __name__ == '__main__':
#     c = con()
    # print(c.beautify_01())