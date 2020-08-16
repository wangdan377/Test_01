# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 19:06
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import unittest
import ddt
from common.http_requests import http_requests
from common.do_excel import do_excel
from requests import exceptions

data = do_excel().get_date()#读取test_data数据
num = 0
@ddt.ddt
class TestHttp01(unittest.TestCase):

    def setUp(self):
        print("----------------------------------------")
    def tearDown(self):
        print("----------------------------------------")

   #使用拆分的数据，发送http_requests请求
    @ddt.data(*data)
    def test_001(self,a):#单接口测试用例
        global num  # 全局变量设置
        num += 1
        try:
            res = http_requests().http_requests(a["http_url"], a["http_mthod"], a["http_param"])
        except exceptions.Timeout as e:# 超时设置
            do_excel().into_date(num + 1, (do_excel().max_column + 1), str(e))#写入超时报错信息
        else:
            print("测试场景：{}".format(a["case"]))
            print("调用的地址是:{}".format(res.url))
            print("请求参数:{}".format((a["http_param"])))
            if res.status_code == 200 :
                print("接口调用成功:",res)
            else:
                print("接口调用失败:{}:".format(res.json()))
            #实际返回结果写入excel
            do_excel().into_date(num + 1, (do_excel().max_column + 1), res.status_code)
            try:
                do_excel().into_date(num + 1, (do_excel().max_column + 2), str(res.json()))
            except:
                do_excel().into_date(num + 1, (do_excel().max_column + 2), "OK")

            self.assertEqual(a["code"],res.status_code,"测试失败")

    def test_002(self):
        pass
if __name__ == "__main__":
    unittest.main()
