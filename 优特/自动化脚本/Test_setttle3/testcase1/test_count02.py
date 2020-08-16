import requests
import unittest
import json,random,string
from Common import request_host
from config_test.config_path import *
from Common import Token
import pytest
import allure
# import ddt
# @ddt.ddt
@allure.feature('123')
class MyTest(unittest.TestCase):
    '''绑定应用—>设置收款账号—>查看用户收款账户'''

    # @ddt.data({'title': 'count2'})
    # @ddt.unpack
    def setUp(self) -> None:
        global app_id
        app_id = ''.join(random.sample(string.ascii_letters + string.digits, 2))
        # global temp
        # temp = ''.join(random.sample(string.ascii_letters + string.digits, 2))

        '''获取token'''
        global headers1
        global headers2
        global headers3
        headers1 = Token.token(1)
        headers2 = Token.token(2)
        headers3 = Token.token(3)

    @allure.story('新建优模型')
    def test_02(self):
        '''绑定应用'''
        bindApp_url = js_url + "/appInfo/bindApp"
        bindApp_data = {"appId": app_id}
        response_bindApp = request_host.get_post(bindApp_url, headers2, bindApp_data)
        '''如果有报错信息,打印报错信息（已存在）,否则 绑定成功'''
        self.assertEqual(200, response_bindApp.status_code, "调用【绑定应用】接口失败。状态码错误")
        print('-------------------应用绑定成功---------------------')

        '''设置用户收款账户'''
        Account_update_url = "https://mobileuat.utcook.com/settle/settlementAccount/update"
        Account_update_data = {
            "account": "{\"recipient\":\"18635943863\",\"recipient_name\":\"wangdan1\"}",
            "appId": "app_abcd123",
            "channelCode": "wx_pub_scan",
            "nickName": "王丹1",
            "type":1
        }
        response_Account_update = request_host.get_post(Account_update_url, headers1, json.dumps(Account_update_data))
        self.assertEqual(200, response_Account_update.status_code, "调用【绑定应用】接口失败。状态码错误")
        print('-------------------设置账号成功---------------------')

        '''查看用户收款账户'''
        Accountget_url = "https://mobileuat.utcook.com/settle/settlementAccount/get"
        Accountget_data = {"appId":"app_abcd123" }
        response_Accountget = request_host.get_get(Accountget_url, headers3, Accountget_data,)
        self.assertEqual(200, response_Accountget.status_code, "调用【绑定应用】接口失败。状态码错误")
        print('-------------------账号查询成功---------------------')


    def tearDown(self) -> None:
        pass




if __name__ == '__main__':
    unittest.main()

