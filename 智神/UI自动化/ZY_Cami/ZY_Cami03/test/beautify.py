from appium import webdriver
import time
class connect(object):
    def connecting01(self):  # 不连接相机/不连接设备
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()  # 相机
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()  # 点击帮助
        driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
        # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
        time.sleep(5)
        return '不连接相机/不连接设备'



