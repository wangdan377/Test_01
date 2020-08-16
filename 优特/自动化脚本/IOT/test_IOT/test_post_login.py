import json
import requests

url = "https://oauthuat.utcook.com/uaa/oauth/login"
headers = {"content-Type":"application/x-www-form-urlencoded",
           "Authorization":"Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0"}
data = {

            "username": "iot_admin_test",
            "password" :"Ut123456",
            "grant_type" : "password",
            "scope":"read"

}
r = requests.post(url=url,headers=headers,data=data)
print(r.json())
# print(r.status_code)
# print(r.text)
s = r.json()["access_token"]    #获取access_token后面的
print(s)
d ="bearer " + s            #前缀+acces token后面的，给d赋值，打印出所有得
print(d)


# url1= "https://mobileuat.utcook.com/iotapp/deviceAdmin/disableThing"
# header1= {"content-Type":"application/json",
#            "Authorization":d}
# data1={
#     "deviceName":"ceshi03",
#     "productKey":"a1wfMsqHljB"
# }
# r1 = requests.post(url=url1,headers=header1,json=data1)
# print(r1.text)
# print(r1.status_code)
# # print(header1)
# print(data1)
#
# # assertEqual(r.get("error_code"), 0) and self.assertEqual(text.get("reason"), "请求成功")
