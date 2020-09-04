# import requests
# import json
#
# login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
# headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
#            "Content-Type": "application/x-www-form-urlencoded"}
# login_data = {"username": "developer_app_admin", "password": "Ut123456", "grant_type": "password",
#               "scope": "read"}
# response = requests.post(url=login_url, headers=headers, data=login_data)
# access_token = response.json()["access_token"]
# Authorization_value = "bearer " + access_token
# global headers1
# global headers2
# global headers3
# headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
# headers2 = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": Authorization_value}
# headers3 = {"Authorization": Authorization_value}
#
#
# w = []
# for i in range(1,6):
#     data={
#         w.append("a" + str(i))
#     }
# print(w)
# print(type(data))
# response= requests.post(url="https://mobileuat.utcook.com/settle/appInfo/bindApp",headers=headers2,data=data)
# print(response.text)
import random
import string
# a= random.randint(2,3)
# print(a)
# index = random.sample(range(0,3),1)
# print(index)

# list = [0,1,2,3,4]
# rs = random.sample(list, 2)
# print(rs)
# print(list)
#
# rs = random.sample(range(0, 9), 4)
# print(rs)

# print(random.random())
# print(random.uniform(1, 10))

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,2)))
print(ran_str)

a=[]
for i in range(1,10):
    a.append(i)
print(a)