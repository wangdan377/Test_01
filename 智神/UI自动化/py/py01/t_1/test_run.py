#coding:utf-8

import unittest

import HTMLTestRunnerCN

suit = unittest.defaultTestLoader.discover(
    start_dir="./test_case",#要执行的目录
    pattern="test_*.py"#目录下test_开头的文件
)
if __name__ == '__main__':
    soundbox_device = 'XYBK01011204300001'
    with open('my_report.html','wb') as fp:
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title="小雅自动化测试报告",
            description='详情',
            tester="石磊",
            device=(soundbox_device),
            verbosity=2  # verbosity参数可以控制执行结果的输出，0是简单报告、1是一般报告、2是详细报告
        )
        # runner = unittest.TextTestRunner()
        runner.run(suit)


