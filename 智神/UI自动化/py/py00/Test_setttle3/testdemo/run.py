'''
@Author: wangdan
@Date: 2020-05-06 15:42:52
@LastEditTime: 2020-05-06 10:11:19
@LastEditors: wangdan
@Description:
@FilePath: \Test_settle\run.py
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #该代码存放的目录
sys.path.append(BASE_DIR)

from HTMLTestRunner import HTMLTestRunner
import unittest
import time,os

if __name__ == "__main__":
    #批量执行的模块
    test_dir='E:\\IOT\\Test_setttle\\testcase'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')   #查找用例

    now=time.strftime('%Y-%m-%d %H_%M_%S')
    #定义报告存放路径
    filename='E:\IOT\Test_setttle\\report\\report'+now+'report.html'
    fp=open(filename,'wb')
    #定义测试报告
    runner=HTMLTestRunner(stream=fp,title='结算云1.0api业务流程测试报告',description='用例执行情况:')
    runner.run(discover,rerun=0, save_last_run=False)
    fp.close()