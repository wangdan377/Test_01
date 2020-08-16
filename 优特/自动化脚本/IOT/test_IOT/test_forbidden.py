import requests
import json
import test_post_login
url = "https://mobileuat.utcook.com/iotapp/deviceAdmin/disableThing"
headers ={"content-Type":"application/json",
           "Authorization":'d'}
data={
    "deviceName":"ceshi03",
    "productKey":"a1wfMsqHljB"
}
r = requests.post(url=url,headers=headers,json=data)
print(r.json())
print(r.status_code)
self.assertEqual(text.get("error_code"), 0) and self.assertEqual(text.get("reason"), "请求成功")