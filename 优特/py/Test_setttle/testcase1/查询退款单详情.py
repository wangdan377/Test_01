import requests
import json
login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
           "Content-Type": "application/x-www-form-urlencoded"}
login_data = {"username": "developer_app_admin", "password": "Ut123456", "grant_type": "password", "scope": "read"}
response = requests.post(url=login_url, headers=headers, data=login_data)
access_token = response.json()["access_token"]
Authorization_value = "bearer " + access_token
global headers1
global headers2
global headers3
headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
headers2 = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": Authorization_value}
headers3 = {"Authorization": Authorization_value}
print(headers1)

# 1绑定应用——>获取开发者全部应用——>设置参数——>查看应用参数——>配置支付渠道参数——>获取支付渠道参数——>添加分润模板——>删除分润模板——>查询分润模板——>查询分润模板列表——>获取应用下所有分润模板
# 2：绑定应用——>设置参数——>配置支付渠道参数——>添加分润模板——>设置收款账号——>创建支付单——>支付成功——>查询支付单详情——>查询支付单列表——>应用方确认收货——>查询结算单详情——>获取交易信息
# 3：绑定应用——>设置收款账号——>查看用户收款账户
# 4:绑定应用——>设置参数——>配置支付渠道参数——>添加分润模板——>设置收款账号——>创建支付单——>未支付——>查询支付单详情——>应用方确认收货——>查询结算单详情
# 5：绑定应用——>设置参数——>配置支付渠道参数——>添加分润模板——>设置收款账号——>创建支付单——>支付成功——>查询支付单——>创建退款单——>查询退款单——>应用方确认收货——>查询结算单详情
# 6：绑定应用——>设置参数——>配置支付渠道参数——>添加分润模板——>设置收款账号——>创建支付单——>支付成功——>应用方确认收货——>创建退款单——>查询退款单——>查询结算单详情
# 7：绑定应用——>设置参数——>配置支付渠道参数——>添加分润模板——>设置收款账号——>创建支付单——>取消支付——>创建退款单——>查询退款单——>应用方确认收货——>查询结算单详情
# 无应用——>去创建支付单
# 无设置参数——>去创建支付单
# 无添加分润模板——>去创建支付单
# 无设置账户——>去创建支付单
# 创建支付单
'''createPayInfo_url = "https://mobileuat.utcook.com/settle/trade/createPayInfo"
createPayInfo_data = {
    "amount":0.01 ,
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
response_createPayInfo = requests.post(url=createPayInfo_url, headers=headers1, json=createPayInfo_data)
print(response_createPayInfo.text)'''
# 应用方确认收货
"""appConfirm_url = "https://mobileuat.utcook.com/settle/trade/appConfirm"
appConfirm_data ={"payNo": "413607740338958336"}
response_appConfirm = requests.post(url=appConfirm_url, headers=headers1, json=appConfirm_data)
print(response_appConfirm.text)"""
# #查询支付单详情（应用开发者）
"""pay_url = "https://mobileuat.utcook.com/settle/pay/get"
pay_data = {"payId":"408168581289816064"}
response_pay = requests.get(url=pay_url, headers=headers1, params=pay_data)
print(response_pay.text)"""

#查询支付单列表（应用开发者）
"""paylist_url = "https://mobileuat.utcook.com/settle/pay/list"
paylist_data = {"appId":"app_abcd123","page":1,"size":1}
response_paylist = requests.get(url=paylist_url, headers=headers1, params=paylist_data)
print(response_paylist.text)"""
# 创建退款单（开发者）
"""createRefundInfo_url = "https://mobileuat.utcook.com/settle/trade/createRefundInfo"
createRefundInfo_data ={
    "remark": "tui1",
    "payNo": "407777925920792576",
    "refundAmount": "0.01"}
response_createRefundInfo = requests.post(url=createRefundInfo_url, headers=headers1, json=createRefundInfo_data)
print(response_createRefundInfo.text)"""
# 退款单详情查询（开发者）
"""refund_url = "https://mobileuat.utcook.com/settle/refund/get"
refund_data ={"refundId":407777925920792576}
responserefund = requests.get(url=refund_url,headers=headers1,params=refund_data)
print(responserefund.text)"""

# 退款单列表查询（开发者）
"""refundlist_url = "https://mobileuat.utcook.com/settle/refund/list"
refundlist_data ={"appId":"app_abcd123", "channelCode":"wx_pub_scan", "page":1, "size":1}
response_refundlist = requests.get(url=refundlist_url, headers=headers1, params=refundlist_data)
print(response_refundlist.text)"""

# #查询结算单列表（应用开发者）
"""settle_list_url = "https://mobileuat.utcook.com/settle/settlement/list"
settle_list_data = {"appId":"app_abcd123","page":1,"size":1}
response_settle_list = requests.get(url=settle_list_url, headers=headers1, params=settle_list_data)
print(response_settle_list.text)"""

# #查询结算单详情（应用开发者）
"""settle_url = "https://mobileuat.utcook.com/settle/settlement/get"
settle_data = {"settlementId":"408079562640011264"}
response_settle = requests.get(url=settle_url, headers=headers3, params=settle_data)
print(response_settle.text)"""

#结算失败处理（应用开发者）
"""settle_failHandle_url = "https://mobileuat.utcook.com/settle/settlement/failHandle"
settle_failHandle_data = {"failureDeal":2, "settlementId":"408079562640011264"}
response_settle_failHandle = requests.post(url=settle_failHandle_url, headers=headers3, data=settle_failHandle_data)
print(response_settle_failHandle.text)"""

# 获取应用交易信息
"""queryAppTradeInfo_url = "https://mobileuat.utcook.com/settle/statistics/queryAppTradeInfo"
response_queryAppTradeInfo = requests.get(url=queryAppTradeInfo_url, headers=headers3)
print(response_queryAppTradeInfo.text)"""

#ping++异步通知结算云（结算云后端）
"""pingAsyncNotify_url = "https://mobileuat.utcook.com/settle/settlement/failHandle"
response_pingAsyncNotify = requests.get(url=pingAsyncNotify_url, headers=headers3)
print(response_pingAsyncNotify.text)"""

#结算失败处理（应用开发者）
"""settleAsyncNotify_url = "https://mobileuat.utcook.com/settle/notify/settleAsyncNotify"
settleAsyncNotify_data = {
    "notifyEvent":"pay",
    "notifyTime":"1587693965450",
    "orderNo":"01234567891",
    "result":"1",
    "tradeNo":"408167094987862016",
    "tradeTime":"1587693965451",
}
response_settleAsyncNotify = requests.post(url=settleAsyncNotify_url, headers=headers1, data=settleAsyncNotify_data)
print(response_settleAsyncNotify.text)"""

#获取应用下所有分润模板
"""queryAppTemplate_url = "https://mobileuat.utcook.com/settle/royaltyTemplate/queryAppTemplate"
queryAppTemplate_data = {"settlementId":"408079562640011264"}
response_queryAppTemplate = requests.get(url=queryAppTemplate_url, headers=headers3, params=queryAppTemplate_data)
print(response_queryAppTemplate.text)"""

#设置用户收款账户
"""settlementAccount_update_url = "https://mobileuat.utcook.com/settle/settlementAccount/update"
settlementAccount_update_data = {
    "account": "{\"recipient\":\"18635943863\",\"recipient_name\":\"wangdan1\"}",
    "appId": "app_abcd123",
    "channelCode": "wx_pub_scan",
    "nickName": "王丹1",
    "type": 1
}
response_settlementAccount_update = requests.post(url=settlementAccount_update_url, headers=headers1, params=settlementAccount_update_data)
print(response_settlementAccount_update.text)"""

#查看用户收款账户
"""Accountget_url = "https://mobileuat.utcook.com/settle/settlementAccount/get"
Accountget_data = {"appId": "app_abcd123"}
response_Accountget = requests.get(url=Accountget_url, headers=headers3, params=Accountget_data)
print(response_Accountget.text)"""
# 开发者绑定应用
"""bindApp_url = "https://mobileuat.utcook.com/settle/appInfo/bindApp"
bindApp_data = {"appId": "a1"}
response_bindApp = requests.post(url=bindApp_url, headers=headers2, params=bindApp_data)
print(response_bindApp.text)
print(type(bindApp_data))"""


# 获取开发者全部应用
"""list_url = "https://mobileuat.utcook.com/settle/appInfo/list"
response_list = requests.get(url=list_url, headers=headers2)
print(response_list.text)"""

# 设置应用参数
"""updateAppInfo_url = "https://mobileuat.utcook.com/settle/appInfo/updateAppInfo"
updateAppInfo_data = {"appId": "11","pingAppId":"app_TevD8SOW5yzHHKK5"}
response_updateAppInfo = requests.post(url=updateAppInfo_url, headers=headers2, params=updateAppInfo_data)
print(response_updateAppInfo.text)"""

# 查询应用参数
'''getAppInfo_url = "https://mobileuat.utcook.com/settle/appInfo/getAppInfo"
getAppInfo_data = {"appId": "1"}
response_getAppInfo = requests.get(url=getAppInfo_url, headers=headers2, params=getAppInfo_data)
print(response_getAppInfo.text)'''
# 配置支付宝渠道参数
"""# updatePayChannel_url = "https://mobileuat.utcook.com/settle/appInfo/updatePayChannel"
# updatePayChannel_data = {"appId": "12", "channelInfo":[{"channelCode": "alipay_scan","channelRate":2}]}
# response_updatePayChannel = requests.post(url=updatePayChannel_url, headers=headers2, params=updatePayChannel_data)
# print(response_updatePayChannel.text)"""
# 获取支付宝渠道参数
"""getPayChannels_url = "https://mobileuat.utcook.com/settle//appInfo/getPayChannels"
getPayChannels_data = {"appId": "12", "channelInfo":[{"channelCode": "alipay","channelRate":3}]}
response_getPayChannels = requests.get(url=getPayChannels_url, headers=headers2, params=getPayChannels_data)
print(response_getPayChannels.text)"""

#添加分润模板
'''Template_create_url = "https://mobileuat.utcook.com/settle/royaltyTemplate/create"
Template_create_data ={
    "appId": "app_abcd123",
    "settleCycle":'0',
    "tempName": "周期0",
    "tempRemark": "0.1元",
    "royaltyRule": [{"role": "平台分润",
            "royaltyMode": "2",
            "value":0.1}]}
response_Template_create = requests.post(url=Template_create_url, headers=headers3, json=Template_create_data)
print(response_Template_create.text)'''

#删除分润模板
"""Template_delete_url='https://mobileuat.utcook.com/settle/royaltyTemplate/delete'
Template_delete_data = {'royaltyTempId':408121091714789376}
response_Template_delete = requests.post(url=Template_delete_url,headers=headers2,params=Template_delete_data)
print(response_Template_delete)"""
#查询分润模板详情
"""royaltyTemplate_url='https://mobileuat.utcook.com/settle/royaltyTemplate/get'
royaltyTemplate_data = {'royaltyTempId':'408121091714789376'}
response_royaltyTemplate = requests.get(url=royaltyTemplate_url,headers=headers2,params=royaltyTemplate_data)
print(response_royaltyTemplate)"""


#查询分润模板列表
"""Template_list_url='https://mobileuat.utcook.com/settle/royaltyTemplate/list'
Template_list_data = {'appId':'app_app123','page':1,'size':2}
response_Template_list = requests.get(url=Template_list_url,headers=headers2,params=Template_list_data)
print(response_Template_list)"""




















