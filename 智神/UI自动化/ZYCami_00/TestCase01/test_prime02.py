#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from PO.login_element import Login_Page
from PO.Prime_Element import Prime_Page
from PO.Edit_Element import Edit_Page
from PO.Activation_page import Activation_Page
from Data.data import *
from Public.loged import *
import unittest,pytest

import time,os,sys
import warnings
from appium.webdriver import Remote
import HTMLTestRunnerCN3_pie_chart_screen
log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')

@ddt  #装饰器类
class Test_Prime_02(unittest.TestCase):
    '''
    未登录状态下，登录-编辑-云剪辑-立即开通-微信支付-关闭
    已登录状态下，编辑-云剪辑-立即开通-微信支付-关闭
    未登录状态下去编辑页面云剪辑，然后购买prime
    已登录状态下，非prime用户，购买一周/二周-协议-隐私政策-购买设备-向上滑动'''
    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod

    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        # cls.driver = appium_desired()     #之前的方法
        # cls.driver.start_activity(appPackage,appActivity)     #另外一种启动方式
        #实例化类
        # self.fun = BaseFun(self.driver)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)    #登录
        self.prime = Prime_Page(self.driver)     #prime
        self.edit = Edit_Page(self.driver)      #edit
        self.action = Activation_Page(self.driver)  # 激活设备
        self.fun = BaseFun(self.driver)


    @data(*get_log_data())      #装饰测试方法，拿到几个数据就可以执行用例

    @unpack                     #根据拿到的数据以都好及逆行拆分
    @pytest.mark.flaky(rerus=3)
    # def test_prime_02_01(self,username,password):
    #     """
    #     未登录状态下，登录-编辑-云剪辑-立即开通-微信支付-关闭
    #     :param username: 账号
    #     :param password: 密码
    #     :return:
    #     """
    #     """try:
    #         self.fun.click(File_name)
    #     except AttributeError:
    #         log.logger.error('访问不到该对象属性')
    #         self.fun.saveScreenshot('camera01')
    #     except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
    #         log.logger.error('元素不存在')
    #         self.fun.saveScreenshot('camera02')
    #     except NoAlertPresentException as b:  # 捕获意外的异常
    #         log.logger.warning('警告')
    #         self.fun.saveScreenshot('camera03')
    #     except Exception as result:
    #         log.logger.critical('严重')
    #         self.fun.saveScreenshot('camera04')
    #     else:
    #         pass  # 没有错的情况下执行
    #     finally:
    #         pass  # 有没有错，都会执行"""
    #     # self.login.click_File_me()        #我的页面icon
    #     self.edit.click_File_Editor()    #底部编辑icon
    #     self.edit.click_File_cloud_engine()  #云剪辑
    #     self.login.click_File_tv_login()
    #     self.login.input_user(username)
    #     self.login.input_password(password)
    #     self.login.click_File_tv_commit()
    #     self.prime.click_File_open01()          #立即开通
    #     self.action.click_File_pay_closed()  # 支付方式关闭
    #     self.action.click_File_wx()             #选择微信支付
    #
    #     # self.prime.click_File_prime01()         #点击【prime】
    #     # self.prime.click_File_year()        #年
    #     # time.sleep(5)
    #     # self.prime.click_File_open01()      #立即开通
    #     # time.sleep(5)
    #     # self.prime.click_File_Service_Agreement()     #服务协议
    #     # self.prime.click_File_Service_Back()        #服务协议返回按钮
    #     # self.prime.click_File_Privacy_Policy()      #隐私政策
    #     # self.prime.click_File_Service_Back()        #隐私政策返回按钮
    #     # time.sleep(2)
    #     # self.fun.swip_left02()                        #向左滑动
    #     # time.sleep(5)
    #     # self.prime.click_File_buy_equipment02()       #购买二设备
    #     # time.sleep(5)
    #     # self.driver.keyevent(4)                     #返回按钮
    #     # time.sleep(2)
    #     # self.fun.swip_up()
    #     # time.sleep(5)
    #
    #
    #
    #     """# self.driver.get_screenshot_as_file('../screen/test_camera.png')   #直接存入报告
    #     self.fun.saveScreenshot('camera')
    #     self.fun.saveScreenshot('help')
    #
    #     self.fun.click(File_enter)"""
    def test_prime_02_02(self,username,password):
        """
        未登录状态下去编辑页面云剪辑，然后购买prime
        :param username: 账号
        :param password: 密码
        :return:
        """
        """try:
            self.fun.click(File_name)
        except AttributeError:
            log.logger.error('访问不到该对象属性')
            self.fun.saveScreenshot('camera01')
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            log.logger.error('元素不存在')
            self.fun.saveScreenshot('camera02')
        except NoAlertPresentException as b:  # 捕获意外的异常
            log.logger.warning('警告')
            self.fun.saveScreenshot('camera03')
        except Exception as result:
            log.logger.critical('严重')
            self.fun.saveScreenshot('camera04')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行"""
        self.login.click_File_me()        #我的页面icon
        # self.login.click_File_Home()    #底部编辑icon
        # self.edit.click_File_cloud_engine()  #云剪辑
        # self.prime.click_File_open01()  # 立即开通
        # self.action.click_File_pay_closed()  # 支付方式关闭
        # self.action.click_File_wx()  # 选择微信支付
        # self.login.click_File_tv_login()
        # self.login.input_user(username)
        # self.login.input_password(password)
        # self.login.click_File_tv_commit()
        # self.prime.click_File_prime01()         #点击【prime】
        # self.prime.click_File_year()        #年
        # time.sleep(5)
        # self.prime.click_File_open01()      #立即开通
        # time.sleep(5)
        # self.prime.click_File_Service_Agreement()     #服务协议
        # self.prime.click_File_Service_Back()        #服务协议返回按钮
        # self.prime.click_File_Privacy_Policy()      #隐私政策
        # self.prime.click_File_Service_Back()        #隐私政策返回按钮
        # time.sleep(2)
        # self.fun.swip_left02()                        #向左滑动
        # time.sleep(5)
        # self.prime.click_File_buy_equipment02()       #购买二设备
        # time.sleep(5)
        # self.driver.keyevent(4)                     #返回按钮
        # time.sleep(2)
        # self.fun.swip_up()
        # time.sleep(5)



        """# self.driver.get_screenshot_as_file('../screen/test_camera.png')   #直接存入报告
        self.fun.saveScreenshot('camera')
        self.fun.saveScreenshot('help')

        self.fun.click(File_enter)"""

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
