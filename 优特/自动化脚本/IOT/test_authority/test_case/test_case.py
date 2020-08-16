# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 14:39
# @Author  : man.jiang
import unittest
import ddt
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from common.http_requests import http_requests
from common.do_excel import do_excel

data = do_excel().get_date()#读取test_data数据
@ddt.ddt
class TestHttp01(unittest.TestCase):

    def setUp(self):
        print("测试开始")
    def tearDown(self):
        print("测试结束")

   #使用拆分的数据，发送http_requests请求
    @ddt.data(*data)
    def test_001(self,a):#单接口测试用例
        res = http_requests().http_requests(a["http_url"], a["http_mthod"], a["http_param"])
        print("调用的地址是:{}".format(res.url))
        if res.status_code == 200 :
            print(res.json())
        else:
            print("接口调用失败,错误：{}".format(res.json()))
        return res
        # self.sheet.cell(row = 2, column = 8, value= res.status_code)
if __name__ == "__main__":
    unittest.main()


