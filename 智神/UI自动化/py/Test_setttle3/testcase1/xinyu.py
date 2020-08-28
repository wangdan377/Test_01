# import requests
# login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
# headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
#            "Content-Type": "application/x-www-form-urlencoded"}
# login_data = {"username": "scf_adm", "password": "Ut123456", "grant_type": "password", "scope": "read"}
# response = requests.post(url=login_url, headers=headers, data=login_data)
# access_token = response.json()["access_token"]
# Authorization_value = "bearer " + access_token
# global headers1
# headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
#
# createModelProfileUsingPOST_url="https://mobileuat.utcook.com/utmodel/modelAdmin/createProfile"
# createModelProfileUsingPOST_param={"category": "ut-device","identifier":"112","name":"更改之前","description": 12}
# createModelProfileUsingPOST=requests.post(url=createModelProfileUsingPOST_url, headers=headers1, json=createModelProfileUsingPOST_param)
# print(createModelProfileUsingPOST.text)

import requests
login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
           "Content-Type": "application/x-www-form-urlencoded"}
login_data = {"username": "stm_dev", "password": "Ut123456", "grant_type": "password", "scope": "read"}
response = requests.post(url=login_url, headers=headers, data=login_data)
access_token = response.json()["access_token"]
Authorization_value = "bearer " + access_token
# global headers3
#
# headers1 = {"Content-Type":"application/json", "Authorization": Authorization_value}
headers3 = {"Authorization": Authorization_value}
# print(headers3)
#
Ac_url = "https://mobileuat.utcook.com/settle/settlementAccount/get"
Ac_data = {"appId":"app_abcd123"}
response_Ac = requests.get(url=Ac_url, headers=headers3, params=Ac_data)
print(response_Ac.text)

