# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 9:13
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from common.http_requests import http_requests

class key_authority_resource_post():

    # 新增 权限空间
    def createAuthSpaceUsingPOST(self,authSpace,authSpaceDesc):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["authSpaceDesc"] = authSpaceDesc
        res = http_requests().http_requests("/auth-internet/resource/createAuthSpace","post", http_param)
        return res
        # 注册资源 tags= {"tagKey_001": "tagValue_0001"}
    def registerResourceUsingPOST(self,authSpace,resourceKey,initKey,tags):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["initKey"] = initKey
        http_param["tags"] = tags
        res = http_requests().http_requests("/auth-internet/resource/registerResource","post", http_param)
        return res
        #设置资源标签
    def setResourceTagsUsingPOST(self,authSpace,resourceKey,tags):
        # 1、当前标签数据库未存在则新增，如例子的size
        # 2、数据库已存在但入参未指定则不改动，如例子的name
        # 3、数据库已存在且入参指定且有值则以入参为准做修改，如例子的color
        # 4、数据库已存在且入参指定但值为空则删除，如例子的hoby
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["tags"] = tags
        res = http_requests().http_requests("/auth-internet/resource/setResourceTags","post", http_param)
        return res
        # 绑定资源
    def bindResourceToUserUsingPOST(self,authSpace,resourceKey,userKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["userKey"] = userKey
        res = http_requests().http_requests("/auth-internet/resource/bindResourceToUser","post", http_param)
        return res
        #解绑资源(用户)
    def unbinResourceToUserUsingPOST(self,authSpace,resourceKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        res = http_requests().http_requests("/auth-internet/resource/unbindResourceToUser","post", http_param)
        return res

class key_authority_resource_get():
    #分页查询 权限空间
    def queryAuthSpaceUsingGET(self):
        res = http_requests().http_requests("/auth-internet/resource/unbindResourceToUser", "get")
        return res
    #获取指定资源的标签列表
    def getResourceTagsUsingGET(self,authSpace,resourceKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        res = http_requests().http_requests("/auth-internet/resource/unbindResourceToUser","get", http_param)
        return res
    #查找指定用户的权限列表
    def getAuthsByUserUsingGET(self,authSpace,userKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["userKey"] = userKey
        res = http_requests().http_requests("/auth-internet/resource/unbindResourceToUser","get", http_param)
        return res
    #查找指定资源的用户列表
    def getUsersByResourceKeyUsingGET(self, authSpace, resourceKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        res = http_requests().http_requests("/auth-internet/resource/unbindResourceToUser","get", http_param)
        return res
    #按标签查询资源列表
    def getResourcesByTagsUsingGET(self, authSpace,tagKey,tagValue):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["tagKey"] = tagKey
        http_param["tagValue"] = tagValue
        http_param["tagKey"] = tagValue
        res = http_requests().http_requests("/auth-internet/resource/unbindResourceToUser","get", http_param)
        return res
    #获取权限文件
    def getAuthorityFileUsingGET(self,authSpace,resourceKey,version):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["version"] = version
        res = http_requests().http_requests("/auth-internet/resource/getAuthorityFile","get", http_param)
        return res

class key_authority_authorize_post():
    #解绑资源（拥有者）
    def unbinResourceUsingPOST(self,authSpace,resourceKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        res = http_requests().http_requests("/auth-internet/authorize/unbinResource","post", http_param)
        return res
    #永久授权（拥有者）
    def permanentUsingPOST(self,authSpace,resourceKey,functionNameList,userKey,shareAble = None):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["functionNameList"] = functionNameList
        http_param["userKey"] = userKey
        http_param["shareAble"] = shareAble
        res = http_requests().http_requests("/auth-internet/authorize/permanent","post", http_param)
        return res
    #限时授权（拥有者）
    def timeLimitedUsingPOST(self,authSpace,resourceKey,functionNameList,userKey,startDateTime,endDateTime,count = None):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["functionNameList"] = functionNameList
        http_param["userKey"] = userKey
        http_param["startDateTime"] = startDateTime
        http_param["endDateTime"] = endDateTime
        http_param["count"] = count
        res = http_requests().http_requests("/auth-internet/authorize/timeLimited","post", http_param)
        return res
    #循环授权（拥有者）
    def timeCircularUsingPOST(self,authSpace,resourceKey,functionNameList,userKey,
                              weekDays,startTime,endTime,startDate,endDate,count = None):
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
        res = http_requests().http_requests("/auth-internet/authorize/timeCircular","post", http_param)
        return res
    #限时权限分享（分享者）
    def timeLimitedShareUsingPOST(self,authSpace,resourceKey,authId,userKey,startDateTime,endDateTime,count = None):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["authId"] = authId
        http_param["userKey"] = userKey
        http_param["startDateTime"] = startDateTime
        http_param["endDateTime"] = endDateTime
        http_param["count"] = count
        res = http_requests().http_requests("/auth-internet/authorize/timeLimitedShare","post", http_param)
        return res
    #循环权限分享（分享者）
    def timeCircularShareUsingPOST(self,authSpace,resourceKey,authId,userKey,
                              weekDays,startTime,endTime,startDate,endDate,count = None):
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
        res = http_requests().http_requests("/auth-internet/authorize/timeCircularShare","post", http_param)
        return res
    #通过分享ID删除分享
    def deleteAuthsByIdUsingPOST(self,authSpace,resourceKey,shareIdList):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["shareIdList"] = shareIdList
        res = http_requests().http_requests("/auth-internet/authorize/deleteAuthsById","post", http_param)
        return res
class key_authority_authorize_get():
    #查看资源绑定状态
    def getResourceBindStatusUsingGET(self,authSpace,resourceKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        res = http_requests().http_requests("/auth-internet/authorize/getResourceBindStatus","get", http_param)
        return res
    #查看分享记录列表
    def listShareRecordsUsingGET(self,authSpace,resourceKey,userKey):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["userKey"] = userKey
        res = http_requests().http_requests("/auth-internet/authorize/listShareRecords","get", http_param)
        return res
    #查找当前用户被授权的资源列表
    def getAuthorizedResourcesUsingGET(self,authSpace,tagKey = None,tagValue= None,valid= None):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param[tagKey] = tagValue
        http_param["valid"] = valid
        res = http_requests().http_requests("/auth-internet/authorize/getAuthorizedResources","get", http_param)
        return res
    #查询指定资源的指定权限是否可用
    def checkAuthUsingGET(self,authSpace,resourceKey,functionName):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["functionName"] = functionName
        res = http_requests().http_requests("/auth-internet/authorize/checkAuth","get", http_param)
        return res
    #查找当前用户的指定资源的功能清单
    def getFunctionsOfResourceUsingGET(self,authSpace,resourceKey,valid = None):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["valid"] = valid
        res = http_requests().http_requests("/auth-internet/authorize/getFunctionsOfResource","get", http_param)
        return res
class key_authority_validate():
    def checkUsingPOST(self,authSpace,resourceKey,authId = None,functionNameList = None):
        http_param = {}
        http_param["authSpace"] = authSpace
        http_param["resourceKey"] = resourceKey
        http_param["authId"] = authId
        http_param["functionNameList"] = functionNameList
        res = http_requests().http_requests("/auth-internet/validate/check","post", http_param)
        return res
if __name__ == '__main__':
    a = key_authority_resource_post()
    # test = a.createAuthSpaceUsingPOST("A291122172123","d191122172123")
    # tags = {}
    test2 =a.bindResourceToUserUsingPOST("A291122172123","test01","userKey01")
    print(test2)
