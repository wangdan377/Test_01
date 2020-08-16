# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 8:08
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from common.http_requests import http_requests

# class key_user:

def  createAppUsingPOST(appKey,name = None,description = None):
    #"新建应用"
    http_param = {}
    http_param["appKey"] = appKey
    http_param["name"] = name
    http_param["description"] = description
    res = http_requests().http_requests ("/user/app/app","post", http_param)
    return res,appKey
    #根据appKey获取应用信息
def getAppInfoUsingGET(self,appKey):
    http_param = {}
    http_param["appKey"] = appKey
    res = http_requests().http_requests ("/user/app/app","get", http_param)
    return res
    #修改应用信息
def updateAppUsingPUT(self,appKey,name = None,description = None):
    http_param = {}
    http_param["appKey"] = appKey
    http_param["name"] = name
    http_param["description"] = description
    res = http_requests().http_requests ("/user/app/app""put", http_param)
    return res
if __name__ == '__main__':
    a = createAppUsingPOST("test1001")
    # a.__int__("/uaa/oauth/login")
    # test1= a.login_requests()
    # test2=a.http_requests("user/user/curUser","get")
    # print(test2)
