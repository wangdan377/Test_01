import requests
import unittest
import json,random,string
from Common import request_host
from config_test.config_path import *
# import ddt
# @ddt.ddt
class MyTest(unittest.TestCase):
    '''绑定应用—>设置收款账号—>查看用户收款账户'''

    # @ddt.data({'title': 'count2'})
    # @ddt.unpack
    def setUp(self) -> None:
        global a1
        a1 = ''.join(random.sample(string.ascii_letters + string.digits, 2))
        login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
        headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
                   "Content-Type": "application/x-www-form-urlencoded"}
        login_data = {"username": "developer_app_admin", "password": "Ut123456", "grant_type": "password",
                      "scope": "read"}
        response = requests.post(url=login_url, headers=headers, data=login_data)
        access_token = response.json()["access_token"]
        Authorization_value = "bearer " + access_token
        global headers1
        global headers2
        global headers3
        headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
        headers2 = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": Authorization_value}
        headers3 = {"Authorization": Authorization_value}
    def test_02(self):
        '''绑定账户'''
        '''绑定应用'''
        bindApp_url = jS_url + "/appInfo/bindApp"
        bindApp_data = {"appId": "28.0"}
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

