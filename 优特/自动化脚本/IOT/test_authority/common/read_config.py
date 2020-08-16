# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 10:46
# @Author  : man.jiang

import configparser
import os
# curpath = os.path.dirname(os.path.realpath(__file__))#当前目录
# curpath = os.path.dirname(curpath)#当前目录的父级目录
# cfgpath = os.path.join(curpath, "config\config.ini")#获取config.ini文件的路径
#
#
# cf = configparser.ConfigParser()#读取config.ini文件数据
# cf.read(cfgpath)
# login_url = cf.get("login_url","login_url")
# http_url = cf.get("http_url","http_url")
# username = cf.get("login_info","username")
# password = cf.get("login_info","password")
# grant_type = cf.get("login_info","grant_type")
# scope = cf.get("login_info","scope")
# login_token = cf.get("login_token","Authorization")
# token_type = cf.get("http_token","token_type")
# access_token = cf.get("http_token","access_token")
# test_data= cf.get("test_data","name")
# wrgpath = os.path.join(curpath, test_data)#获取word.xlsx文件的路径
# print(wrgpath)
# #设置登陆数据
# login_param = {}
# login_param["username"] = username
# login_param["password"] = password
# login_param["grant_type"] = grant_type
# login_param["scope"] = scope
# #设置登陆的header数据
# login_header = {}
# login_header["Authorization"] = login_token
# #设置登陆失败，默认的header数据
# http_header = {}
# http_header["Authorization"] = token_type
# test_token = token_type + " " + access_token
# http_header["Authorization"] = test_token

class get_common:
    def __init__(self,url = "config\config.ini"):
        self.curpath = os.path.dirname(os.path.realpath(__file__))#当前目录
        self.curpath = os.path.dirname(self.curpath)#当前目录的父级目录
        self.cfgpath = os.path.join(self.curpath, url)#获取config.ini文件的路径
        self.cf = configparser.ConfigParser()#读取config.ini文件数据
        self.cf.read(self.cfgpath,encoding="utf-8-sig")#支持中文读取

    def get_login_url(self):  # login_url
        login_url = self.cf.get("login_url","login_url")
        return login_url

    def get_http_url(self):  # login_url
        http_url = self.cf.get("http_url","http_url")
        return http_url

    def get_login_param(self): #设置登陆数据
        username = self.cf.get("login_info", "username")
        password = self.cf.get("login_info", "password")
        grant_type = self.cf.get("login_info", "grant_type")
        scope = self.cf.get("login_info", "scope")
        curUser = self.cf.get("login_info", "curUser")
        return username,password,grant_type,scope,curUser

    def get_login_header(self):#设置登陆的header数据
        login_token = self.cf.get("login_token","Authorization")
        login_header = {}
        login_header["Authorization"] = login_token
        return login_header

    def get_header(self):  #设置登陆失败，默认的header数据
        token_type = self.cf.get("http_token","token_type")
        access_token = self.cf.get("http_token","access_token")
        test_data = self.cf.get("test_data","name")
        http_header = {}
        http_header["Authorization"] = token_type
        test_token = token_type + " " + access_token
        http_header["Authorization"] = test_token
        return http_header,test_data

    def get_excel(self):# 获取word.xlsx文件
        excel_data = self.cf.get("excel_data", "excel_url")
        excel_url = os.path.join(self.curpath, excel_data)
        sheet = self.cf.get("excel_data", "sheet")
        return excel_url,sheet

if __name__ == '__main__':
    a = get_common().get_excel()
    print(a)
