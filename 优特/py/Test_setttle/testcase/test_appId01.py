import requests
import unittest
import json,string,random
from Common import request_host
from config_test.config_path import *

class MyTest(unittest.TestCase):
    '''[绑定应用]—>获取开发者全部应用—>设置参数—>查看应用参数—>配置支付渠道参数—>获取支付渠道参数—>添加分润模板—>删除分润模板—>查询分润模板—>查询分润模板列表—>获取应用下所有分润模板'''

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
    def test_01(self):
        '''绑定应用'''
        bindApp_url = jh_url + "/appInfo/bindApp"
        bindApp_data = {'appId': a1}
        response_bindApp = request_host.get_post(bindApp_url, headers2, bindApp_data)
        self.assertEqual(200, response_bindApp.status_code, "调用【绑定应用】接口失败。状态码错误")
        if 'utMsg' in response_bindApp.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % ((response_bindApp.status_code), response_bindApp.json()))
        else:
            print('绑定成功')

        '''获取开发者全部应用'''
        list_url = jh_url +"settle/appInfo/list"
        response_list = request_host.get_post(list_url, headers3)
        # '''如果有报错信息，该用户不存在。否则 查询出详情（只判断权限）'''
        if "utMsg"  in response_list.text:
             raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % ((response_list.status_code), json.dumps(response_list.json())))
        else:
            print('获取全部应用列表')

        '''设置应用参数'''
        updateAppInfo_url =  "https://mobileuat.utcook.com/settle/appInfo/updateAppInfo"
        updateAppInfo_data = {"appId": "11","pingAppId":"app_TevD8SOW5yzHHKK6"}
        response_updateAppInfo = request_host.get_post(updateAppInfo_url, headers2, updateAppInfo_data)
        print(response_updateAppInfo.text)
        '''如果有报错信息,打印报错信息（已设置）,否则 设置成功'''
        if 'utMsg' in response_updateAppInfo.text:
            raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' %((response_updateAppInfo.status_code),response_updateAppInfo.json()))
        else:
            print('参数设置成功')

        '''查询应用参数'''
        getAppInfo_url = "https://mobileuat.utcook.com/settle/appInfo/getAppInfo"
        getAppInfo_data = {"appId": "1"}
        response_getAppInfo = request_host.get_get(getAppInfo_url, headers3, getAppInfo_data)
        '''如果有报错信息,打印报错信息（409）,否则 查询成功'''
        if 'utMsg' in response_getAppInfo.text:
            raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' %((response_getAppInfo.status_code),response_getAppInfo.json()))
        else:
            if "1" != response_getAppInfo.json()["appId"]:
                raise ValueError("编辑后，未修改成功，状态码为 %s, 返回信息为：%s" %
                                 ((response_getAppInfo.status_code),response_getAppInfo.json()))
            else:
                print("查询参数")

        '''配置支付宝渠道参数'''
        updatePayChannel_url = "https://mobileuat.utcook.com/settle/appInfo/updatePayChannel"
        updatePayChannel_data = {"appId": "1", "channelInfo":[{"channelCode": "alipay","channelRate":2}]}
        response_updatePayChannel = request_host.get_post(updatePayChannel_url, headers1, json.dumps(updatePayChannel_data))
        '''如果有报错信息,打印报错信息（配置错误）,否则 配置成功'''
        if 'utMsg' in response_updatePayChannel.text:
            raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' %(
                (response_updatePayChannel.status_code),response_updatePayChannel.json()))
        else:
            print('配置支付渠道')

        '''获取支付宝渠道参数'''
        getPayChannels_url = "https://mobileuat.utcook.com/settle/appInfo/getPayChannels"
        getPayChannels_data = {"appId": "1", "channelInfo":[{"channelCode": "alipay","channelRate":6}]}
        response_getPayChannels = request_host.get_get(getPayChannels_url, headers3, getPayChannels_data)
        '''如果有报错信息,打印报错信息（409）,否则 配置成功'''
        if 'utMsg' in response_getPayChannels.text:
            raise ValueError('调用 接口失败，状态码为: %s ,返回信息为：%s' %
                             ((response_getPayChannels.status_code), response_getPayChannels.json()))
        else:
            if "2.0" != str(response_getPayChannels.json()[1]["channelRate"]):
                raise ValueError("编辑后，未修改成功，状态码为 %s, 返回信息为：%s" %(
                    (response_getPayChannels.status_code),response_getPayChannels.json()))
            else:
                print("获取支付渠道信息")
        '''添加分润模板'''
        Template_create_url = "https://mobileuat.utcook.com/settle/royaltyTemplate/create"
        Template_create_data = {
            "appId": "app_abcd123",
            "settleCycle": '0',
            "tempName": "周期1.3",
            "tempRemark": "0.1元",
            "royaltyRule": [{"role": "平台分润",
                             "royaltyMode": "2",
                             "value": 0.1}]}
        response_Template_create = request_host.get_post(Template_create_url, headers1, json.dumps(Template_create_data))
        '''如有报错，打印报错信息（1005），否则 添加成功'''
        self.assertEqual(200, response_Template_create.status_code, "调用【添加模板】接口失败。状态码错误")
        if 'utMsg' in response_Template_create.text:
            raise ValueError('调用 接口失败，状态码为: %s,返回信息为 %s' %((response_Template_create.status_code),response_Template_create.json()))
        else:
            print('分润模板添加成功')
        '''删除分润模板'''
        Template_delete_url='https://mobileuat.utcook.com/settle/royaltyTemplate/delete'
        Template_delete_data = {'royaltyTempId':408121091714789376}
        response_Template_delete = request_host.get_post(Template_delete_url, headers2, Template_delete_data)
        '''如果有报错信息，打印报错信息（409）,否则 删除成功'''
        if 'utMsg' in response_Template_delete.text:
            raise ValueError('调用 接口失败，状态码为: %s,返回信息为 %s' %((response_Template_delete.status_code),response_Template_delete.json()))
        else:
            print('删除分润')
        '''查询分润模板详情'''
        royaltyTemplate_url='https://mobileuat.utcook.com/settle/royaltyTemplate/get'
        royaltyTemplate_data = {'royaltyTempId':'408121091714789376'}
        response_royaltyTemplate = request_host.get_get(royaltyTemplate_url, headers2, royaltyTemplate_data)
        '''如果报错，打印报错信息（409），否则 查询成功'''
        if 'utMsg' in response_royaltyTemplate.text:
            raise ValueError('调用 接口失败，状态码为: %s,返回信息为 %s' %((response_royaltyTemplate.status_code),response_royaltyTemplate.json()))
        else:
            print('查询分润模板详情')
        '''查询分润模板列表'''
        Template_list_url='https://mobileuat.utcook.com/settle/royaltyTemplate/list'
        Template_list_data = {'appId':'app_app123','page':1,'size':2}
        response_Template_list = request_host.get_get(Template_list_url, headers2, Template_list_data)
        '''如果报错，返回报错信息（409），否则查询成功'''
        if 'utMsg' in response_Template_list.text:
            raise ValueError('调用 接口失败，状态码为: %s,返回信息为 %s' %((response_Template_list.status_code),response_Template_list.json()))
        else:
            print('查询分润模板列表')
    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()








