import requests
import unittest
import json
from Common import request_host
from HTMLTestRunner import HTMLTestRunner
from config_test.config_path import *

class MyTest(unittest.TestCase):
    '''绑定应用——>获取开发者全部应用——>设置参数——>查看应用参数——>配置支付渠道参数——>获取支付渠道参数——>添加分润模板——>删除分润模板——>添加分润模板——>查询分润模板——>查询分润模板列表——>获取应用下所有分润模板'''

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
        # """绑定应用"""
        # bindApp_url = jh_url +"/appInfo/bindApp"
        # bindApp_data = {"appId": "12"}
        # response_bindApp = request_host.request(bindApp_url, headers2, bindApp_data, typed="post")
        # print(response_bindApp.text)
        # """如果有报错信息,打印报错信息（已存在）,否则 绑定成功"""
        #
        # if "utMsg"  in response_bindApp.text:
        #      raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % ((response_bindApp.status_code), response_bindApp.json()))
        # else:
        #     print('绑定成功')

        # '''获取开发者全部应用'''
        # list_url = jh_url +"/appInfo/list"
        # response_list = request_host.request(url=list_url, headers=headers3)
        # print(response_list.text)
        # '''如果有报错信息，该用户不存在。否则 查询出详情（只判断权限）'''
        # if "utMsg"  in response_list.text:
        #      raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % ((response_list.status_code), response_list.json()))
        # else:
        #     print('获取全部')

        # '''设置应用参数'''
        # updateAppInfo_url = jh_url + "appInfo/updateAppInfo"
        # updateAppInfo_data = {"appId": "app_abcd123","pingAppId":"app_TevD8SOW5yzHHKK3"}
        # response_updateAppInfo = request_host.request(updateAppInfo_url, headers2, updateAppInfo_data)
        # print(response_updateAppInfo.text)
        # """如果有报错信息,打印报错信息（已经设置）,否则 设置成功"""
        # if 'utMsg' in response_updateAppInfo.text:
        #     raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' %((response_updateAppInfo.status_code),response_updateAppInfo.json()))
        # else:
        #     print('设置成功')
        # #
        # '''查询应用参数'''
        # getAppInfo_url = jh_url +"/appInfo/getAppInfo"
        # getAppInfo_data = {"appId": "11"}
        # response_getAppInfo = request_host.request(getAppInfo_url, headers3, getAppInfo_data)
        # print(response_getAppInfo.text)
        # """如果有报错信息,打印报错信息（已存在）,否则 设置成功"""
        # if 'utMsg' in response_getAppInfo.text:
        #     raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' %((response_getAppInfo.status_code),response_getAppInfo.json()))
        # else:
        #     if "更改之后" != response_getAppInfo.text:
        #         raise ValueError("编辑后，未修改成功，状态码为 %s, 返回信息为：%s" %((response_getAppInfo.status_code),response_getAppInfo.json()))
        #     else:
        #         print("200")
        #
        # 配置支付宝渠道参数
        # updatePayChannel_url = jh_url + "appInfo/updatePayChannel"
        # updatePayChannel_data = {"appId": "1", "channelInfo":[{"channelCode": "alipay","channelRate":2}]}
        # response_updatePayChannel = request_host.request(updatePayChannel_url, headers2, updatePayChannel_data)
        # print(response_updatePayChannel.text)
        # """如果有报错信息,打印报错信息（配置错误）,否则 配置成功"""
        # if 'utMsg' in response_updatePayChannel.text:
        #     raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' %(
        #         (response_updatePayChannel.status_code),response_updatePayChannel.json()))
        # else:
        #     print('配置成功')
        #
        # # 获取支付宝渠道参数
        getPayChannels_url = "https://mobileuat.utcook.com/settle//appInfo/getPayChannels"
        getPayChannels_data = {"appId": "1", "channelInfo":[{"channelCode": "alipay","channelRate":6}]}
        response_getPayChannels = request_host.request(getPayChannels_url, headers3, getPayChannels_data)
        """如果有报错信息,打印报错信息（配置错误）,否则 配置成功"""
        if 'utMsg' in response_getPayChannels.text:
            raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' % (
            (response_getPayChannels.status_code), response_getPayChannels.json()))
        else:
            if "2.0" != str(response_getPayChannels.json()[0]["channelRate"]):
                raise ValueError("编辑后，未修改成功，状态码为 %s, 返回信息为：%s" %(
                    (response_getPayChannels.status_code),response_getPayChannels.json()))
            else:
                print("200")

        # print(response_getPayChannels.json()[0]["channelRate"])


    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()








