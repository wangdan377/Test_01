#!/usr/bin/python
# -*- coding: utf-8 -*-

# 给网站加一个默认的url地址前缀
# 比如我们的测试都是对github.com这个网站来做的，那么脚本案例2的写法，我们每个请求里都要写一边完整的url,'http://github.com/login','http://github.com/xxx',这使代码显得有些冗余。因此我们阔以建一个类，自动给所有url加上前缀
import requests,json
'''2,get,post等各种http方法,用于用户使用,但这里并没有真正实现这些方法,因为这些方法都是在requests里有实现过.我们只要把参数传给requests就行了,这个传递我们写在requets方法里,所以这里的http方法都是条用requests方法
3,request方法:真正调用self.session的各种方法,这里同样是把参数传下去,只是在传之前,给所有用户输入的url加了一个前缀,前缀的值是用户在init方法里输入的'''
class RestClient():
    def __init__(self,api_root_url):
        '''
        1,init方法：初始化这个类，初始化的时候需要输入api_root_url，也就是URL的前缀。
        另外还在初始化时创建了self.session用于保存requests的session
        :param api_root_url:
        '''
        self.api_root_url = api_root_url
        self.session = requests.session()
    def get(self,url,**kwargs):
        return self.request(url,'get',**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return self.request(url,'post',data,json,**kwargs)
    def options(self,url,**kwargs):
        return self.request(url,'options',**kwargs)
    def head(self,url,**kwargs):
        return self.request(url,'head',**kwargs)
    def put(self,url,data=None,**kwargs):
        return self.request(url,'put',data,**kwargs)
    def patch(self,url,data=None,**kwargs):
        return self.request(url,'patch',data,**kwargs)
    def delete(self,url,**kwargs):
        return self.request(url,'delete',**kwargs)
    def request(self,url,method_name,data=None,json=None,**kwargs):
        url = self.api_root_url+url
        if method_name == 'get':
            return self.session.get(url,**kwargs)
        if method_name == 'post':
            return self.session.post(url,data,json,**kwargs)
        if method_name == 'options':
            return self.session.options(url,**kwargs)
        if method_name == 'head':
            return self.session.head(url,**kwargs)
        if method_name == 'put':
            return self.session.put(url,data,**kwargs)
        if method_name == 'patch':
            return self.session.patch(url,data,**kwargs)
        if method_name == 'delete':
            return self.session.delete(url,**kwargs)
r = RestClient('http://httpbin.org')
# x =r.post('/post',json = {'a':'b'})
# print(x.text)

x1 = r.get('/get',json = {'a':'b'})
print(x1.text)

# requests请求示例
# r=requests.post('http://httpbin.org/post',json={'a':'b'})
# print(r.text)
