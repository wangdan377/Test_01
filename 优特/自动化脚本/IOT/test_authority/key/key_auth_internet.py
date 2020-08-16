# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 9:21
# @Author  : man.jiang
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 9:13
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from common.http_requests import http_requests
from common import DB
# 新增 权限空间
def createAuthSpaceUsingPOST(authSpace,authSpaceDesc):
    data = DB.DB_COM().Select_Table("auth-internet", "createAuthSpaceUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["authSpaceDesc"] = authSpaceDesc
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
    # 注册资源 tags= {"tagKey_001": "tagValue_0001"}
def registerResourceUsingPOST(authSpace,resourceKey,tags):
    data = DB.DB_COM().Select_Table("auth-internet", "registerResourceUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["tags"] = tags
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
    #设置资源标签
def setResourceTagsUsingPOST(authSpace,resourceKey,tags):
    # 1、当前标签数据库未存在则新增，如例子的size
    # 2、数据库已存在但入参未指定则不改动，如例子的name
    # 3、数据库已存在且入参指定且有值则以入参为准做修改，如例子的color
    # 4、数据库已存在且入参指定但值为空则删除，如例子的hoby
    data = DB.DB_COM().Select_Table("auth-internet", "setResourceTagsUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["tags"] = tags
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
    # 绑定资源
def bindResourceToUserUsingPOST(authSpace,resourceKey,userKey):
    data = DB.DB_COM().Select_Table("auth-internet", "bindResourceToUserUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["userKey"] = userKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
    #解绑资源(用户)
def unbinResourceToUserUsingPOST(authSpace,resourceKey):
    data = DB.DB_COM().Select_Table("auth-internet", "unbinResourceToUserUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#分页查询 权限空间
def queryAuthSpaceUsingGET():
    data = DB.DB_COM().Select_Table("auth-internet", "unbinResourceToUserUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    res = http_requests().http_requests(http_url,data["http_mthod"])
    return res
#获取指定资源的标签列表
def getResourceTagsUsingGET(authSpace,resourceKey):
    data = DB.DB_COM().Select_Table("auth-internet", "getResourceTagsUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#查找指定用户的权限列表
def getAuthsByUserUsingGET(authSpace,userKey):
    data = DB.DB_COM().Select_Table("auth-internet", "getAuthsByUserUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["userKey"] = userKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#查找指定资源的用户列表
def getUsersByResourceKeyUsingGET(authSpace, resourceKey):
    data = DB.DB_COM().Select_Table("auth-internet", "getUsersByResourceKeyUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#按标签查询资源列表
def getResourcesByTagsUsingGET(authSpace,tagKey,tagValue):
    data = DB.DB_COM().Select_Table("auth-internet", "getResourcesByTagsUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["tagKey"] = tagKey
    http_param["tagValue"] = tagValue
    http_param["tagKey"] = tagValue
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#获取权限文件
def getAuthorityFileUsingGET(authSpace,resourceKey,version):
    data = DB.DB_COM().Select_Table("auth-internet", "getAuthorityFileUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["version"] = version
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#解绑资源（拥有者）
def unbinResourceUsingPOST(authSpace,resourceKey):
    data = DB.DB_COM().Select_Table("auth-internet", "unbinResourceUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#永久授权（拥有者）
def permanentUsingPOST(authSpace,resourceKey,functionNameList,userKey,shareAble = None):
    data = DB.DB_COM().Select_Table("auth-internet", "permanentUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["functionNameList"] = functionNameList
    http_param["userKey"] = userKey
    http_param["shareAble"] = shareAble
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#限时授权（拥有者）
def timeLimitedUsingPOST(self,authSpace,resourceKey,functionNameList,userKey,startDateTime,endDateTime,count = None):
    data = DB.DB_COM().Select_Table("auth-internet", "timeLimitedUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["functionNameList"] = functionNameList
    http_param["userKey"] = userKey
    http_param["startDateTime"] = startDateTime
    http_param["endDateTime"] = endDateTime
    http_param["count"] = count
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#循环授权（拥有者）
def timeCircularUsingPOST(authSpace,resourceKey,functionNameList,userKey,
                          weekDays,startTime,endTime,startDate,endDate,count = None):
    data = DB.DB_COM().Select_Table("auth-internet", "timeCircularUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["functionNameList"] = functionNameList
    http_param["userKey"] = userKey
    http_param["weekDays"] = weekDays
    http_param["startTime"] = startTime
    http_param["endTime"] = endTime
    http_param["startDate"] = startDate
    http_param["endDate"] = endDate
    http_param["count"] = count
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#限时权限分享（分享者）
def timeLimitedShareUsingPOST(self,authSpace,resourceKey,authId,userKey,startDateTime,endDateTime,count = None):
    data = DB.DB_COM().Select_Table("auth-internet", "timeLimitedShareUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["authId"] = authId
    http_param["userKey"] = userKey
    http_param["startDateTime"] = startDateTime
    http_param["endDateTime"] = endDateTime
    http_param["count"] = count
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#循环权限分享（分享者）
def timeCircularShareUsingPOST(self,authSpace,resourceKey,authId,userKey,
                          weekDays,startTime,endTime,startDate,endDate,count = None):
    data = DB.DB_COM().Select_Table("auth-internet", "timeCircularShareUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["authId"] = authId
    http_param["userKey"] = userKey
    http_param["weekDays"] = weekDays
    http_param["startTime"] = startTime
    http_param["endTime"] = endTime
    http_param["startDate"] = startDate
    http_param["endDate"] = endDate
    http_param["count"] = count
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#通过分享ID删除分享
def deleteAuthsByIdUsingPOST(self,authSpace,resourceKey,shareIdList):
    data = DB.DB_COM().Select_Table("auth-internet", "deleteAuthsByIdUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["shareIdList"] = shareIdList
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#查看资源绑定状态
def getResourceBindStatusUsingGET(self,authSpace,resourceKey):
    data = DB.DB_COM().Select_Table("auth-internet", "getResourceBindStatusUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#查看分享记录列表
def listShareRecordsUsingGET(self,authSpace,resourceKey,userKey):
    data = DB.DB_COM().Select_Table("auth-internet", "listShareRecordsUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["userKey"] = userKey
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#查找当前用户被授权的资源列表
def getAuthorizedResourcesUsingGET(self,authSpace,tagKey = None,tagValue= None,valid= None):
    data = DB.DB_COM().Select_Table("auth-internet", "getAuthorizedResourcesUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param[tagKey] = tagValue
    http_param["valid"] = valid
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#查询指定资源的指定权限是否可用
def checkAuthUsingGET(self,authSpace,resourceKey,functionName):
    data = DB.DB_COM().Select_Table("auth-internet", "checkAuthUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["functionName"] = functionName
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
#查找当前用户的指定资源的功能清单
def getFunctionsOfResourceUsingGET(self,authSpace,resourceKey,valid = None):
    data = DB.DB_COM().Select_Table("auth-internet", "getFunctionsOfResourceUsingGET")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["valid"] = valid
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
def checkUsingPOST(self,authSpace,resourceKey,authId = None,functionNameList = None):
    data = DB.DB_COM().Select_Table("auth-internet", "checkUsingPOST")
    http_url = "/" + data["codea"] + data["http_url"]
    http_param = {}
    http_param["authSpace"] = authSpace
    http_param["resourceKey"] = resourceKey
    http_param["authId"] = authId
    http_param["functionNameList"] = functionNameList
    res = http_requests().http_requests(http_url,data["http_mthod"], http_param)
    return res
if __name__ == '__main__':
    pass
