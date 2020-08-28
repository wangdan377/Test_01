import requests
import unittest
import json
from Common import request_host


class MyTest(unittest.TestCase):
    '''绑定应用—>设置参数—>配置支付渠道参数—>添加分润模板—>设置收款账号—>创建支付单—>未支付—>查询订单详情—>应用方确认收货—>查询结算单详情'''
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
    def test_04(self):
        '''未支付进行结算'''
        '''绑定应用'''
        bindApp_url = jh_url + "/appInfo/bindApp"
        bindApp_data = {"appId": "29.0"}
        response_bindApp = request_host.get_post(bindApp_url, headers2, bindApp_data)
        '''如果有报错信息,打印报错信息（已存在）,否则 绑定成功'''
        self.assertEqual(200, response_bindApp.status_code, "调用【绑定应用】接口失败。状态码错误")
        if 'utMsg' in response_bindApp.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % ((response_bindApp.status_code), response_bindApp.json()))
        else:
            print('绑定成功')

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
        response_Template_create = request_host.get_post(Template_create_url, headers1,
                                                         json.dumps(Template_create_data))
        '''如有报错，打印报错信息（1005），否则 添加成功'''
        self.assertEqual(200, response_Template_create.status_code, "调用【添加模板】接口失败。状态码错误")
        if 'utMsg' in response_Template_create.text:
            raise ValueError(
                '调用 接口失败，状态码为: %s,返回信息为 %s' % ((response_Template_create.status_code), response_Template_create.json()))
        else:
            print('分润模板添加成功')

        '''设置用户收款账户'''
        Account_update_url = "https://mobileuat.utcook.com/settle/settlementAccount/update"
        Account_update_data = {
            "account": "{\"recipient\":\"18635943863\",\"recipient_name\":\"wangdan1\"}",
            "appId": "app_abcd123",
            "channelCode": "wx_pub_scan",
            "nickName": "王丹1",
            "type": 1
        }
        response_Account_update = request_host.get_post(Account_update_url, headers1, json.dumps(Account_update_data))
        if 'utMsg' in response_Account_update.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % ((response_Account_update.status_code), response_Account_update.json()))
        else:
            print('账号设置成功')

        '''创建支付单'''
        createPayInfo_url = "https://mobileuat.utcook.com/settle/trade/createPayInfo"
        createPayInfo_data = {
            "amount": 0.01,
            "appId": "app_abcd123",
            "goodsDesc": "1",
            "channelCode": "alipay",
            "clientIp": "192.168.2.126",
            "remark": "无模板",
            "orderNo": "012345678913",
            "goodsName": "未",
            "extra": {},
            "royalty": {
                "royaltyTempId": "398703675838615552",
                "royaltyDetail": [{"role": "平台分润",
                                   "userId": "stm_dev"}]}}
        response_createPayInfo = request_host.get_post(createPayInfo_url, headers1, json.dumps(createPayInfo_data))
        if 'utMsg' in response_createPayInfo.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % (response_createPayInfo.status_code), response_createPayInfo.json())
        else:
            print('未支付')
        '''查询支付单详情（应用开发者）'''
        pay_url = "https://mobileuat.utcook.com/settle/pay/get"
        pay_data = {"payId":"408168581289816064"}
        response_paylist = request_host.get_get(pay_url, headers3, pay_data)
        if 'utMsg' in response_paylist.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % (response_paylist.status_code),
                             response_paylist.json())
        else:
            print('支付成功')


        '''应用方确认收货'''
        appConfirm_url = "https://mobileuat.utcook.com/settle/trade/appConfirm"
        appConfirm_data = {"payNo": "410681497356423168"}
        response_appConfirm = request_host.get_post(appConfirm_url, headers1, json.dumps(appConfirm_data))
        self.assertEqual(200, response_appConfirm.status_code, "调用【确认收货】接口失败。状态码错误")
        if 'utMsg' in response_appConfirm.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % (response_appConfirm.status_code),
                             response_appConfirm.json())
        else:
            print('结算成功')
        '''查询结算单详情（应用开发者）'''
        settle_url = "https://mobileuat.utcook.com/settle/settlement/get"
        settle_data = {"settlementId":"408079562640011264"}
        response_paylist = request_host.get_get(settle_url, headers3, settle_data)
        if 'utMsg' in response_paylist.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % (response_paylist.status_code),
                             response_paylist.json())
        else:
            print('结算详情')
        '''获取应用交易信息'''
        queryAppTradeInfo_url = "https://mobileuat.utcook.com/settle/statistics/queryAppTradeInfo"
        response_queryAppTradeInfo = request_host.get_get(queryAppTradeInfo_url, headers3)
        if 'utMsg' in response_queryAppTradeInfo.text:
            raise ValueError("调用  接口失败,状态码为: %s ,返回信息为：%s" % (response_queryAppTradeInfo.status_code),
                             response_queryAppTradeInfo.json())
        else:
            print('获取交易信息')

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()