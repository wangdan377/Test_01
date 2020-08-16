import requests
import unittest
import json
from Common import request_get
from config_test import *

class MyTest(unittest.TestCase):

    def setUp(self) -> None:

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
    def test_01(self):
        """创建应用"""
        bindApp_url = "https://mobileuat.utcook.com/settle/appInfo/bindApp"
        bindApp_data = {"appId": "app_abcd123", "pingAppId": "app_1234561237123445"}
        response_bindApp = requests.post(url=bindApp_url, headers=headers2, params=bindApp_data)
            """如果没有报错信息,说明该应用已经存在,否则设置参数
                    如果有报错信息,说明格式不对,修改后创建应用"""
        if "utMsg" not in response_bindApp.json():


            # self.assertEqual(200, deleteModelProfileByKeyUsingPOST.status_code, "调用  删除优模型  接口失败。状态码错误")
            """这里进行判断， 删除成功的话返回为空。如果出现报错信息，说明接口调用错误"""
            if "utMsg" in response_bindApp.json.text:
                raise ValueError("调用   删除优模型接口  失败,状态码为: %s ,返回信息为：%s" % (
                (deleteModelProfileByKeyUsingPOST.status_code), deleteModelProfileByKeyUsingPOST.json()))
            else:
                """设置参数"""
                createModelProfileUsingPOST_url = jh_url + "/modelAdmin/createProfile"
                createModelProfileUsingPOST_param = {"category": "ut-device", "identifier": "112", "name": "更改之前",
                                                     "description": description, "modelSource": "unilink"}
                createModelProfileUsingPOST = request_frame_work.request1(createModelProfileUsingPOST_url, headers1,
                                                                          createModelProfileUsingPOST_param,
                                                                          typed="post")
                self.assertEqual(200, createModelProfileUsingPOST.status_code, "调用  进行创建优模型  接口失败。状态码错误")
        else:
            """设置参数"""
            bindApp_url = "https://mobileuat.utcook.com/settle/appInfo/bindApp"
            bindApp_data = {"appId": "app_abcd123", "pingAppId": "app_1234561237123445"}
            response_bindApp = requests.post(url=bindApp_url, headers=headers2, params=bindApp_data)




