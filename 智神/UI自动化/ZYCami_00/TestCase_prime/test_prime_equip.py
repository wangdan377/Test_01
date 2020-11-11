#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from PO.login_element import Login_Page
from PO.Prime_Element import Prime_Page
from Public.Prime_Pay import Prime_Pay
from Public.Wx_Pay import Wx_Config
from PO.Wx_Element import Wx_Page
from Public.Prime_Equipment import Prime_Buy_Equipment
from Public.Prime_Equit_Member import Prime_Equit_Members
from Public.Prime_Equit_Member  import Prime_Equit_Members
from Public.Prime_Me_Member  import Prime_Members
from Data.data import *
from Public.loged import *
import unittest,pytest
import time,os,sys
import warnings
from appium.webdriver import Remote
import HTMLTestRunnerCN3_pie_chart_screen


# @ddt  #装饰器类
class Test_Prime_equip(unittest.TestCase):
    '''已登录则进入prime页面，未登录则去登录
    不是会员则选择套餐购买，是会员则进行续费
    '''
    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        #实例化类
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)    #登录
        self.prime = Prime_Page(self.driver)     #prime
        self.fun = BaseFun(self.driver)
        self.logins = LogIn(self.driver)
        self.prime_pays = Prime_Pay(self.driver)
        self.wx_pays = Wx_Config(self.driver)   #微信支付密码
        self.prime_buy_equipment = Prime_Buy_Equipment(self.driver)   #购买设备
        self.wx = Wx_Page(self.driver)
        self.equit_member = Prime_Equit_Members(self.driver)       #是否会员
    # @data(*get_log_data())      #装饰测试方法，拿到几个数据就可以执行用例
    # @unpack                     #根据拿到的数据以都好及逆行拆分
    # @pytest.mark.flaky(rerus=3)
    def test_prime_equit(self):
        # 判断是否登录，如果已登录，则继续执行。如果未登录则进行登录
        try:
            self.login.click_File_me()
            self.prime.click_File_prime01()
            time.sleep(5)
        except:
            self.logins.login_01()
            self.prime.click_File_prime01()

        finally:
            self.equit_member.prime_equit_user()   #是否登录员都会执行,是否会员
            time.sleep(5)


    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
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
