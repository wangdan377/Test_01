#coding:utf-8
import time,os
import unittest
import HTMLTestRunner
import HTMLTestRunner2
import HTMLTestRunnerCN
import HTMLTestRunnerCN3

import HTMLTestRunnerCN3_pie_chart_screen2

suit = unittest.defaultTestLoader.discover(
    # start_dir="D:\py\ZY_Cami\\test_case",#要执行的目录
    start_dir="../test_case",
    pattern="test_*.py"#目录下test_开头的文件
)
if __name__ == '__main__':
    #直接放在运行的文件夹(test_demo)里
    """soundbox_device = 'XYBK01011204300001'
    with open('my_report.html', 'wb') as fp:
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title='zy自动化测试报告',
            description='详情',
            tester='啊哈',
            device=(soundbox_device),
            verbosity=2  # verbosity参数可以控制执行结果的输出，0是简单报告、1是一般报告、2是详细报告
        )
        # runner = unittest.TextTestRunner()
        runner.run(suit)
        fp.close()"""

# HTMLTestRunner,无tester device标题,无饼图

    """now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况:')
    # runner.run(suit, rerun=0, save_last_run=False)
    runner.run(suit)
    fp.close()"""

#HTMLTestRunnerCN生成的测试报告,有tester device标题,没饼图
    """soundbox_device = 'XYBK01011204300001'
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    # filename = os.getcwd() + os.sep + 'report'+ os.sep + 'report' + now + 'result.html'
    filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',device=(soundbox_device),description='用例执行情况:')
    runner.run(suit)
    # 关闭报告
    fp.close()"""


# 这个是HTMLTestRunner2方法生成的报告，无tester device标题,有饼图
#     报错
    """now = time.strftime('%Y-%m-%d %H_%M_%S')
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    # filename = os.getcwd() + os.sep + 'report'+ os.sep + 'report' + now + 'result.html'  #第一种方法
    filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'  # 第二种方法
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunner2.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况:')
    # runner.run(suit, rerun=0, save_last_run=False)
    runner.run(suit)
    fp.close()"""

# HTMLTestRunnerCN3,有title,tester标题+饼图
    """soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹', device=(soundbox_device), description='用例执行情况:')
    # runner.run(suit, rerun=0, save_last_run=False)
    runner.run(suit)
    fp.close()"""

# 这个是HTMLTestRunnerCN3_pie_chart_screen2,有title,tester标题+饼图+美观+截图
#     --------------->在test_case方法目录下面 - ----------
    """soundbox_device = 'XYBK01011204300001'
        with open('my_report.html', 'wb') as fp:
            runner = HTMLTestRunnerCN3_pie_chart_screen2.HTMLTestRunner(
                stream=fp,
                title='zy自动化测试报告',
                description='详情',
                tester='啊哈',
                device=(soundbox_device),
                verbosity=2  # verbosity参数可以控制执行结果的输出，0是简单报告、1是一般报告、2是详细报告
            )
            # runner = unittest.TextTestRunner()
            runner.run(suit)
            fp.close()"""

    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    # filename = os.getcwd() + os.sep+ 'report' + now + 'result.html'    #相对路径
    filename = '../report' + os.sep + 'report' + now + 'result.html'   #在上级目录report文件夹下
    # filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'   #绝对路径
    
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen2.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹', device=(soundbox_device),
                                              description='用例执行情况:')
    # runner.run(suit, rerun=0, save_last_run=False)
    runner.run(suit)
    fp.close()




