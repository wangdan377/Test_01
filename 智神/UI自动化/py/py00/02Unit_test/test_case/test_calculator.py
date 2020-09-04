#!usr/bin/env python3
#-*- coding:utf-8 _*-
"""
@author:shilei
@file: test_calculator.py
@time: 2020/08/18

__author__ = "lei.shi@ximalaya.com"
"""
import HTMLTestRunnerCN
import HTMLTestRunnerCN3
import HTMLTestRunnerCN
import unittest
import calculator
import time
import os
import sys
#创建子类继承unittest.TestCase,然后重写以下方法
#父类的东西子类继承之后，self直接调用
class ModuleTest(unittest.TestCase):
    # 注意所有测试方法都需要以test开头,否则是不被unittest识别的
    # setUp、tearDown 这两个方法在每个测试方法执行前以及执行后执行一次，
    # setUp用来为测试准备环境，tearDown用来清理环境，已备之后的测试
    def setUp(self):
        print('start test')
        self.cal = calculator.Calculator(3,2)
    def tearDown(self):

        print('end test')
        pass
    # 实现方法：装饰器
    # 强制跳过，不需要判断条件。reason是跳过原因的描述必须填写
    # @unittest.skip("不想执行这个case")
    def test_add(self):

        res = self.cal.add()
        self.assertEqual(res,5)
        # name = 'test1'
        # path_1 = os.getcwd() + os.sep + 'screen' + os.sep + name + '.png'
        # path_2 = os.getcwd() + os.sep + 'screen' + os.sep + sys._getframe().f_code.co_name + '.png'
        # print(path_1, path_2)
        # if os.rename(path_1, path_2):
        #     pass
        # else:
        #     pass

    def test_sub(self):

        res = self.cal.sub()
        self.assertEqual(res,1)

    def test_mul(self):
        res = self.cal.mul()
        self.assertEqual(res, 6)

    def test_div(self):
        res = self.cal.div()
        self.assertEqual(res, 1.5)
    def test_add1(self):
        res = self.cal.add()
        # self.assertRegex(str(res),'[0-9]')
        self.assertRegex(str(res),'5')
        # name = 'test2'
        # path_1 = os.getcwd() + os.sep + 'screen' + os.sep + name + '.png'
        # path_2 = os.getcwd() + os.sep + 'screen' + os.sep + sys._getframe().f_code.co_name + '.png'
        # print(path_1, path_2)
        # if os.rename(path_1, path_2):
        #     pass
        # else:
        #     pass
# 使用TestCase实现将测试根据其测试的功能分组在一起。 unittest为此提供了一种机制：测试套件
def Suit():
    suite = unittest.TestSuite()
    # 构造测试集
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest('test_sub'))
    suite.addTest(ModuleTest('test_mul'))
    suite.addTest(ModuleTest('test_div'))
    suite.addTest(ModuleTest('test_add1'))
    return suite

# if __name__ == '__main__':

    """soundbox_device = 'XYBK01011204300001'
    path = './report'+os.sep+'report-'+time.strftime('%m%d-%H:%M:%S')+'.html'
    with open(path,'wb') as fp:
        # runner = HTMLTestRunnerCN.HTMLTestRunner(
        # runner = HTMLTestRunnerCN3.HTMLTestRunner(
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title="计算器自动化测试报告",
            description='详情',
            tester="石磊",
            device=(soundbox_device),
            verbosity=2  # verbosity参数可以控制执行结果的输出，0是简单报告、1是一般报告、2是详细报告
        )
        runner.run(Suit())"""