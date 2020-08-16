import requests
import json
from Common import request_host
from config_test.config_path import *

def token(s1):
    login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
    headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
               "Content-Type": "application/x-www-form-urlencoded"}
    login_data = {"username": "stm_dev", "password": "Ut123456", "grant_type": "password",
                  "scope": "read"}
    response = requests.post(url=login_url, headers=headers, data=login_data)
    access_token = response.json()["access_token"]
    Authorization_value = "bearer " + access_token
    if s1 ==1:
        headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
        return headers1
    elif s1 ==2:
        headers2 = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": Authorization_value}
        return headers2
    else:
        headers3 = {"Authorization": Authorization_value}
        return headers3



