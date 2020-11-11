
#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from PO.login import *
from PO.login_element import Login_Page
from Data.data import *
from Public.loged import *
import unittest,pytest
import time,os,sys
import warnings
import HTMLTestRunnerCN3_pie_chart_screen
# log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
class Test_Login_01(unittest.TestCase):

    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        # cls.driver = appium_desired()     #之前的方法
        # cls.driver.start_activity(appPackage,appActivity)     #另外一种启动方式
        #实例化类
        # self.fun = BaseFun(self.driver)
        driver = Caplictily.Driver_Config()
        cls.driver = driver.get_driver()
        cls.fun = BaseFun(cls.driver)
        cls.login = Login_Page(cls.driver)
        # driver = Caplictily.Driver_Config()
        # self.driver = driver.get_driver()
        # self.login = Login_page(self.driver)
        # self.fun = BaseFun(self.driver)

    def test_login_01(self):
        self.login.click_File_me()
        # self.login.click_File_tv_login()
        # self.fun.send_keys(File_et_name,username)
        # self.fun.send_keys(File_et_pass,password)
        # self.login.click_File_tv_commit()

    # 关闭驱动
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
    """suite = unittest.TestSuite()
    suite.addTest(Camera_test("test_camera"))
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = '../report/' + now + 'result.html'  # 第一种方法,相对路径下
    '''# filename = '../report/report' + now + 'result.html'  # 第二种方法,相对路径下+report报告名字
    # filename = '../report'+ os.sep+ 'report' + now + 'result.html'    #第二种方法,相对路径下,上级目录../report文件夹下,分隔符下文件名  os.sep+ 'report'
    # filename = os.getcwd() + os.sep+ 'report' + now + 'result.html'   #相对路径下,该路径下的,所以就到test_case下面了
    # filename = os.path.dirname(os.path.dirname(__file__))+ os.sep + 'report' + now + 'result.html'  #相对路径下,该路径下的,所以就到test_case下面了
    # filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'   #绝对路径下
    # filename = '../' + now + 'result.html'   #../是上级目录,还是在上级目录下
    # filename = '../' + os.sep + 'report' + now + 'result.html'   #还是在上级目录下
    # filename = '../report' + now + 'result.html'  #还是在上级目录下'''
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',
                                                               device=(soundbox_device),
                                                               description='用例执行情况:')
    runner.run(suite)
    # runner.run(Suit())
    fp.close()"""

