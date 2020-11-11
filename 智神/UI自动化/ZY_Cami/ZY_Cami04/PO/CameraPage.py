# coding=utf-8
__author__ = 'JennyHui'

from appium import webdriver
from selenium.webdriver.common.by import By
from PO import BasePage

'''
好豆菜谱首页涉及的所有页面元素 - 操作方法 -> 封装
'''
driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.Base.desired_caps)


class Dash(BasePage.Base):
    #相机按钮
    camera_loc =(By.ID,"com.zhiyun.cama:id/iv_camera")
    #driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()   #正常的元素
    # print(camera_loc)
    """#帮助
    # help_loc = (By.ID, "com.zhiyun.cama:id/ib_hel")
    # #不连设备,直接进入拍照
    # enter_loc = (By.ID, "com.zhiyun.cama:id/enter")"""

    # 点击【相机】按钮，连接设备
    def click_camera_loc(self):
        self.find_elements(self.camera_loc)
        return''
    """# 点击【帮助】，进入帮助页面
    def click_help_loc(self):
        self.find_elements(self.help_loc)

    # 未连接设备，点击【直接进入】
    def click_enter_loc(self):
        self.find_elements(self.enter_loc)
"""
dash = Dash('driver')
dash.click_camera_loc()

    # 搜索/收藏


"""def search(recipe):
    dash_page = Dash(driver)
    dash_page.click_search_box()
    print(u'搜索关键字:' + recipe)
    dash_page.input_recipe(recipe)
    driver.press_keycode(66)
    dash_page.click_clloect_item()
    dash_page.click_favorite_clloect()
    dash_page.get_recipe_name()
    dash_page.saveScreenshot('search_' + recipe)
    driver.quit()
"""