'''
目标：实现登录接口对象封装
'''
import requests

# 新建类 登录接口对象
class ApiLogin(object):
    # 新建方法 登录方法
    def api_post_login(self,url,username,password,grant_type,scope):
        headers = {"content-Type":"application/x-www-form-urlencoded",
           "Authorization":"Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0"}
        data = {"username":username,"password":password,"grant_type":grant_type,"scope":scope}
        #调用post并返回响应对象
        return requests.post(url,headers=headers,data=data)
