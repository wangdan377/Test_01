# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 17:45
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from common import DB
from common.http_requests import http_requests
class key_user:
    #登录用户信息【公用】
    def getLoginUserUsingGET(self ):
        data = DB.DB_COM().Select_Table("user","getLoginUserUsingGET")
        http_url = "/" + data["codea"] + data["http_url"]
        res = http_requests().http_requests(http_url,data["http_mthod"])
        return res.json()

    def createAppUsingPOST(self,appKey,name = None,description = None ):
        data = DB.DB_COM().Select_Table("user","createAppUsingPOST")
        http_url = "/" + data["codea"] + data["http_url"]
        http_param = {}
        http_param["appKey"] = appKey
        http_param["name"] = name
        http_param["description"] = description
        res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
        return res.json()

if __name__ == '__main__':
    test = key_user().getLoginUserUsingGET()
    print(test)
