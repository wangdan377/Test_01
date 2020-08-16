# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 15:02
# @Author  : man.jiang
import unittest
import time
import HTMLTestRunnerNew
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from test_case.test_case_sit import TestHttp01
from test_case.test_case_authority import authority_TEST01
loader = unittest.TestLoader()#创建测试加载器
suite = unittest.TestSuite()#创建测试包
suite.addTest(loader.loadTestsFromTestCase(TestHttp01))#加载整个测试类      #跑这个
# suite.addTest(loader.loadTestsFromTestCase(authority_TEST))
# suite.addTest(authority_TEST01("test_004"))#加载整个单个用例

localtime = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())#获取当前时间
with open(localtime +".html","wb+") as file:
    runner  = HTMLTestRunnerNew.HTMLTestRunner(stream = file,
                                          title = "测试报告",
                                          description ="测试用",
                                          tester = "JM")
    runner .run(suite)

