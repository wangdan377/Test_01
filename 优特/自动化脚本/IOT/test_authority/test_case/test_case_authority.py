# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 16:12
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import unittest
import datetime
from key.key_authority import *
now = datetime.datetime.now()
Datetime = now.strftime("%Y%m%d%H%M%S")  # 获取当前时间
class authority_TEST01(unittest.TestCase):
    def setUp(self):
        print("测试开始")
    def tearDown(self):
        print("测试结束")
        # 新增 权限空间
    def test_001(self):
        authSpace = "A" + Datetime  # 按时间戳设定authSpace
        authSpaceDesc = "D" + Datetime  # 按时间戳设定description
        res = key_authority_resource_post().createAuthSpaceUsingPOST(authSpace,authSpaceDesc)
        if  res.status_code ==  200:
            print("新增 权限空间成功，权限空间为：{}".format(authSpace))
        else:
            print("新增权限空间失败：{}".format(res.json()))
        return authSpace
        #注册资源
    def test_002(self):
        resourceKey = "R" + Datetime  # 按时间戳设定resourceKey
        authSpace = authority_TEST01().test_001()
        tags = {}
        tagKey = "K"+ Datetime
        tagValue = "v"+ Datetime
        initKey = 1
        tags[tagKey] = tagValue
        res = key_authority_resource_post().registerResourceUsingPOST(authSpace,resourceKey ,initKey,tags)
        if  res.status_code ==  200:
            print("注册资源成功，资源信息为：{}".format(resourceKey ))
        else:
            print("注册资源失败{}".format(res.json()))
        return authSpace,resourceKey
        # 设置资源标签,变更tagKey信息
    def test_003(self):
        test = authority_TEST01().test_002()
        authSpace = test[0]
        resourceKey = test[1]
        tags = {}
        tagKey = "K"+ Datetime
        tagValue = "v"+ Datetime
        tags[tagKey] = tagValue
        res = key_authority_resource_post().setResourceTagsUsingPOST(authSpace,resourceKey,tags)
        if  res.status_code ==  200:
            print("设置资源标签成功：{}".format(tags))
        else:
            print(res.json())
        return authSpace,resourceKey
        # 绑定资源
    def test_004(self):
        test = authority_TEST01().test_003()
        authSpace = test[0]
        resourceKey = test[1]
        userKey = "jiangman"
        res = key_authority_resource_post().bindResourceToUserUsingPOST(authSpace,resourceKey,userKey)
        if  res.status_code ==  200:
            print("资源绑定成功，绑定人员为：{}".format(userKey))
        else:
            print(res.json())
        return authSpace,resourceKey,userKey
    #删除资源绑定
    def test_005(self):
        test = authority_TEST01().test_004()
        authSpace = test[0]
        resourceKey = test[1]
        res = key_authority_resource_post().unbinResourceToUserUsingPOST(authSpace,resourceKey)
        if  res.status_code ==  200:
            print("解绑成功，资源{}现无绑定人员".format(resourceKey))
        else:
            print(res.json())
# class authority_TEST02(unittest.TestCase):
#     authSpace = authority_TEST01().test_004()[0] #获取已绑定资源的空间信息
#     resourceKey = authority_TEST01().test_004()[1]#获取已绑定资源的资源信息
#     userKey = authority_TEST01().test_004()[2]#获取已绑定资源的人员信息
#     #解绑资源
#     def test001(self):
#         res = key_authority_authorize_post().unbinResourceUsingPOST(self.authSpace, self.resourceKey)
#         if  res.status_code ==  200:
#             print("{}解绑成功".format(self.resourceKey))
#         else:
#             print(res.json())
    #拥有者永久授权
    def test006(self):
        test = authority_TEST01().test_004()
        authSpace = test[0]
        resourceKey = test[1]
        functionNameList = ["function01","function02"]#设置功能信息
        userKey = "user_share"#被永久授权人员信息
        shareAble = "true"#被永久授权人员拥有分享权限
        res = key_authority_authorize_post().permanentUsingPOST(authSpace,resourceKey,functionNameList,userKey,shareAble)
        if  res.status_code ==  200:
            print("永久权限成功,{}功能，已绑定{}".format(functionNameList,userKey))
            return authSpace,resourceKey,res
        else:
            print("授权失败",res.json())
    #拥有者限时授权
    def test007(self):
        test = authority_TEST01().test_004()
        authSpace = test[0]
        resourceKey = test[1]
        functionNameList = ["function01","function02"]#设置功能信息
        userKey = "user_used01"#被限时授权人员信息
        startDateTime = now.strftime("%Y-%m-%d %H:%M")#获取当前时间
        endDateTime = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")#当前时间+1天
        print(startDateTime,endDateTime)
        res = key_authority_authorize_post().timeLimitedUsingPOST(authSpace,resourceKey,functionNameList,userKey,startDateTime,endDateTime,count = 2)
        if  res.status_code ==  200:
            print("限时授权成功,{}功能，已绑定{}".format(functionNameList,userKey))
        else:
            print(res.json())
    #拥有者循环授权
    def test008(self):
        test = authority_TEST01().test_004()
        authSpace = test[0]
        resourceKey = test[1]
        functionNameList = ["function01","function02"]
        userKey = "user_used01"
        weekDays = [now.weekday(),now.weekday()+2]#获取当前星期，及星期+2天
        startTime = now.strftime("%H:%M") # 获取当前年月日
        endTime = (now + datetime.timedelta(hours = 1)).strftime("%H:%M")#当前年月日+1天
        startDate = now.strftime("%Y-%m-%d")#获取当前时分
        endDate = (now + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")#当前小时+1
        print(startTime,endTime)
        res = key_authority_authorize_post().timeCircularUsingPOST(authSpace,resourceKey,functionNameList,userKey,
                                                                   weekDays,startTime,endTime,startDate,endDate,count = None)
        if  res.status_code ==  200:
            print("永久权限分享成功,{}功能，已绑定{}".format(functionNameList,userKey))
        else:
            print(res.json())
    #分享者限时分享
    def test009(self):
        test = authority_TEST01().test006()
        authSpace = test[0]
        resourceKey = test[1]
        authId = test[2]
        userKey = "user02"#被限时授权人员信息
        startDateTime = datetime.datetime.now()#获取当前时间
        endDateTime = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")#当前时间+1天
        res = key_authority_authorize_post().timeLimitedShareUsingPOST(authSpace,resourceKey,authId,userKey,startDateTime,endDateTime,count = None)
        if  res.status_code ==  200:
            print("永久权限分享成功,{}功能，已绑定{}".format(authId,userKey))
        else:
            print(res.json())
    #分享者循环分享
    def test010(self):
        test = authority_TEST01().test006()
        authSpace = test[0]
        resourceKey = test[1]
        authId = test[2]
        userKey = "user02"#被循环授权人员信息
        startDateTime = datetime.datetime.now()#获取当前时间
        weekDays = [startDateTime.weekday(),startDateTime.weekday()+2]#获取当前星期，及星期+2天
        startTime = startDateTime.strftime("%Y%m%d")# 获取当前年月日
        endTime = (startDateTime + datetime.timedelta(days = 1)).strftime("%Y%m%d")#当前年月日+1天
        startDate = startDateTime.strftime("%H:%M")#获取当前时分
        endDate = (startDateTime + datetime.timedelta(hours = 1)).strftime("%H:%M")#当前小时+1
        res = key_authority_authorize_post().timeCircularShareUsingPOST(authSpace,resourceKey,authId,userKey,
                                                                   weekDays,startTime,endTime,startDate,endDate,count = None)
        if  res.status_code ==  200:
            print("永久权限分享成功,{}功能，已绑定{}".format(authId,userKey))
        else:
            print(res.json())
    #按ID删除分享
    def test011(self):
        test = authority_TEST01().test006()
        authSpace = test[0]
        resourceKey = test[1]
        shareIdList = []
        shareIdList.insert(0,test[2].json())
        res = key_authority_authorize_post().deleteAuthsByIdUsingPOST(authSpace,resourceKey,shareIdList)
        if  res.status_code ==  200:
            print("{}绑定已删除".format(shareIdList))
        else:
            print(res.json())
# if __name__ == '__main__':
#     unittest.main()
