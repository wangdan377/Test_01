import requests
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

# 一：绑定应用——>设置参数——>编辑参数——>查询参数——>配置支付费率——>编辑支付费率——>查询支付费率——>添加分润模板——>删除分润模板单详情
# 二：绑定应用——>绑定账户——>创建支付单——>确认收货——>查询结算单详情

# #查询支付单详情（应用开发者）
# pay_url = "https://mobileuat.utcook.com/settle/pay/get"
# pay_data = {"payId":"408168581289816064"}
# response_pay = requests.get(url=pay_url, headers=headers1, params=pay_data)
# print(response_pay.text)
#
# #查询支付单列表（应用开发者）
# paylist_url = "https://mobileuat.utcook.com/settle/pay/list"
# paylist_data = {"appId":"app_abcd123","page":1,"size":1}
# response_paylist = requests.get(url=paylist_url, headers=headers1, params=paylist_data)
# print(response_paylist.text)

# 退款单详情查询（开发者）
# refund_url = "https://mobileuat.utcook.com/settle/refund/get"
# refund_data ={"refundId":407777925920792576}
# responserefund = requests.get(url=refund_url,headers=headers1,params=refund_data)
# print(responserefund.text)

# 退款单列表查询（开发者）
# refundlist_url = "https://mobileuat.utcook.com/settle/refund/list"
# refundlist_data ={"appId":"app_abcd123", "channelCode":"wx_pub_scan", "page":1, "size":1}
# response_refundlist = requests.get(url=refundlist_url, headers=headers1, params=refundlist_data)
# print(response_refundlist.text)

# #查询结算单列表（应用开发者）
# settle_list_url = "https://mobileuat.utcook.com/settle/settlement/list"
# settle_list_data = {"appId":"app_abcd123","page":1,"size":1}
# response_settle_list = requests.get(url=settle_list_url, headers=headers1, params=settle_list_data)
# print(response_settle_list.text)

# #查询结算单详情（应用开发者）
# settle_url = "https://mobileuat.utcook.com/settle/settlement/get"
# settle_data = {"settlementId":"408079562640011264"}
# response_settle = requests.get(url=settle_url, headers=headers3, params=settle_data)
# print(response_settle.text)

#结算失败处理（应用开发者）
# settle_failHandle_url = "https://mobileuat.utcook.com/settle/settlement/failHandle"
# settle_failHandle_data = {"failureDeal":2, "settlementId":"408079562640011264"}
# response_settle_failHandle = requests.post(url=settle_failHandle_url, headers=headers3, data=settle_failHandle_data)
# print(response_settle_failHandle.text)

# 获取应用交易信息
# queryAppTradeInfo_url = "https://mobileuat.utcook.com/settle/statistics/queryAppTradeInfo"
# response_queryAppTradeInfo = requests.get(url=queryAppTradeInfo_url, headers=headers3)
# print(response_queryAppTradeInfo.text)

#ping++异步通知结算云（结算云后端）
# pingAsyncNotify_url = "https://mobileuat.utcook.com/settle/settlement/failHandle"
# response_pingAsyncNotify = requests.get(url=pingAsyncNotify_url, headers=headers3)
# print(response_pingAsyncNotify.text)

#结算失败处理（应用开发者）
# settleAsyncNotify_url = "https://mobileuat.utcook.com/settle/notify/settleAsyncNotify"
# settleAsyncNotify_data = {
#     "notifyEvent":"pay",
#     "notifyTime":"1587693965450",
#     "orderNo":"01234567891",
#     "result":"1",
#     "tradeNo":"408167094987862016",
#     "tradeTime":"1587693965451",
# }
# response_settleAsyncNotify = requests.post(url=settleAsyncNotify_url, headers=headers1, data=settleAsyncNotify_data)
# print(response_settleAsyncNotify.text)

#获取应用下所有分润模板
# queryAppTemplate_url = "https://mobileuat.utcook.com/settle/royaltyTemplate/queryAppTemplate"
# queryAppTemplate_data = {"settlementId":"408079562640011264"}
# response_queryAppTemplate = requests.get(url=queryAppTemplate_url, headers=headers3, params=queryAppTemplate_data)
# print(response_queryAppTemplate.text)

#设置用户收款账户
# settlementAccount_update_url = "https://mobileuat.utcook.com/settle/settlementAccount/update"
# settlementAccount_update_data = {
#     "account": "{\"recipient\":\"18635943863\",\"recipient_name\":\"wangdan1\"}",
#     "appId": "app_abcd123",
#     "channelCode": "wx_pub_scan",
#     "nickName": "王丹1",
#     "type": 1
# }
# response_settlementAccount_update = requests.post(url=settlementAccount_update_url, headers=headers1, params=settlementAccount_update_data)
# print(response_settlementAccount_update.text)

#设置用户收款账户
# settlementAccount_url = "https://mobileuat.utcook.com/settle/settlementAccount/get"
# settlementAccount_data = {"appId": "app_abcd123"}
# response_settlementAccount = requests.get(url=settlementAccount_url, headers=headers3, params=settlementAccount_data)
# print(response_settlementAccount.text)

# 开发者绑定应用
bindApp_url = "https://mobileuat.utcook.com/settle/appInfo/bindApp"
bindApp_data = {"appId": "app_abcd123","pingAppId":"app_1234561237123445"}
response_bindApp = requests.post(url=bindApp_url, headers=headers2, params=bindApp_data)
print(response_bindApp.text)

#设置应用参数
# updateAppInfo_url = "https://mobileuat.utcook.com/settle/appInfo/updateAppInfo"
# updateAppInfo_data = {"appId": "app_abcd123"}
# response_updateAppInfo = requests.post(url=updateAppInfo_url, headers=headers2, params=updateAppInfo_data)
# print(response_updateAppInfo.text)














