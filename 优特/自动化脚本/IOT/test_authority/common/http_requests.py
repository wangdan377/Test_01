# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 9:59
# @Author  : man.jiang
import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from common.read_config import get_common

class http_requests():
    username_ini = get_common().get_login_param()[0]
    password_ini = get_common().get_login_param()[1]
    grant_type_ini = get_common().get_login_param()[2]
    scope_ini = get_common().get_login_param()[3]
    curUser_ini =get_common().get_login_param()[4]
    def login_requests(self,url = "/uaa/oauth/login",username = username_ini ,password = password_ini ,grant_type = grant_type_ini):
        '''调用config初始化数据'''
        url = get_common().get_login_url() + url
        header = get_common().get_login_header()
        param = {}
        param["username"] = username
        param["password"] = password
        param["grant_type"] = grant_type
        res = requests.post(url, param, headers = header) #发送登陆https请求
        #根据登返回的数据，设置后续接口header
        if res.status_code == 200 and  "access_token" in res.json():
            http_header = {}
            http_header["Authorization"] = res.json()["token_type"] +" "+ res.json()["access_token"]
            http_header = http_header
            return http_header
            #密码、账号错误,设置默认后续接口header
        else:
            print("登陆失败，错误信息：{}".format(res.json()))

   #公用调用接口
    def http_requests(self,http_url,http_mthod,http_param = None,http_header = None):
        url = get_common().get_http_url() + http_url  # 调用config初始化数据
        print(url)
        if http_header == None:
            http_header = http_requests().login_requests()#调用login_requests函数
            http_header["curUser"] = self.curUser_ini
        else:
            http_header = http_header
        if http_mthod == "get":#判定请求类型
            res = requests.get(url,http_param ,headers = http_header)
        elif http_mthod == "post":
            res = requests.post(url,json=http_param,headers = http_header)
        elif http_mthod == "put":
            res = requests.put(url,json=http_param,headers = http_header)
        elif http_mthod == "delete":
            res = requests.delete(url,json=http_param,headers = http_header)
        else:
            res = None
            print("未找到合适请求方式")
        return res

        # 互联网权限调用接口
    def http_requests_auth(self, http_url, http_mthod, http_param=None, http_header=None):
        url = get_common().get_http_url() + http_url  # 调用config初始化数据
        if  http_header == None:
            http_header = http_requests().login_requests()  # 调用login_requests函数
        else:
            http_header = http_header
        http_header["curUser"] = self.username_ini
        if http_mthod == "get":  # 判定请求类型
            res = requests.get(url, http_param, headers=http_header)
        elif http_mthod == "post":
            res = requests.post(url, json=http_param, headers=http_header)
        elif http_mthod == "put":
            res = requests.put(url, json=http_param, headers=http_header)
        elif http_mthod == "delete":
            res = requests.delete(url, json=http_param, headers=http_header)
        else:
            res = None
            print("未找到合适请求方式")
        return res

if __name__ == '__main__':
    print(sys.path)
    '''a = http_requests()
    test1 = a.login_requests(url = "/uaa/oauth/login",username = "jiangman01" ,password = "jJ123456" )
    data = {}
    for A in range (100,102):
        data["authSpace"] = "test_" + str(A)
        test3 = a.http_requests("/auth-internet/resource/createAuthSpace","post",data,http_header = test1 )
        print(test3.json())'''
    import ddt
    print(ddt)
