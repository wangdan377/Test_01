#!usr/bin/env python3
#-*- coding:utf-8 _*-
"""
@author:shilei
@file: test_calculator.py
@time: 2020/08/18

__author__ = "lei.shi@ximalaya.com"
"""
import HTMLTestRunnerCN
import HTMLTestRunner
import unittest

import now

import calculator
import time

class ModuleTest(unittest.TestCase):
    #测试准备前要做的工作和测试执行完后要做的工作.包括setUp()和tearDown()
    #setUp()和tearDown() 将在每个测试中被调用一次
    def setUp(self):
        print('start test')

        self.cal = calculator.Calculator(3,2)
    def tearDown(self):
        print('end test')
        pass
    def test_add(self):

        res = self.cal.add()
        self.assertEqual(res,5)
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
'''
return [
            (u'测试人员', self.tester),
            (u'被测设备号', self.device),
            (u'开始时间', startTime),
            (u'合计耗时', duration),
            (u'测试结果', status + "，通过率= " + self.passrate),
        ]
'''
if __name__ == '__main__':

    soundbox_device = '7HX0219918017044'
    path = time.strftime('%m-%d-%H-%M-%S')
    # filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'
    with open('my_report.html','wb') as fp:
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title="计算器自动化测试报告",
            description='详情',
            tester="石磊",
            device=(soundbox_device),
            verbosity=2  # verbosity参数可以控制执行结果的输出，0是简单报告、1是一般报告、2是详细报告
        )
        # runner = unittest.TextTestRunner()
        runner.run(Suit())