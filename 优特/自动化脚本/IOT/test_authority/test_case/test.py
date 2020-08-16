# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 10:15
# @Author  : man.jiang

# basester = 'helloWorld'
# print(basester[1:-1])
# print(basester[5:])
# print(basester[-3:])
# print(basester[::4])

# ageinfo = {"age1":"18","age2":"18","age3":"24"}
# print(ageinfo.get("age2"))
# print(ageinfo["age2"])
# print(ageinfo.items())
# print(ageinfo.keys())
# print(ageinfo)

# sex = "gril"
# if(sex=="boy"):
#     print("say:hello boy!")
# else:
#     print("say:hello gril!")

# city = "ZhuHai"
# if(city == "ZhuHai"):
#     print("go ZhuHai")
# elif(city == "ShenZhen"):
#     print("I love ShenZhen")
# elif(city == "ShangHai"):
#     print("....")
# else:
#     print("what?")
# count = 0

# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print('当前水果 :', fruits[index])
# print("Good bye!")


# def say_hello():
#     print("hello wrold")
#
# #函数调用
# say_hello()

# def fun_plus(a,b):
#     return  a+b
# print(fun_plus(1,2))

# import requests
#
# #发送无参数的get请求,尝试获取某个网页
# r = requests.get('http://www.baidu.com')
# #发送无参数的get请求 设置超时时间 timeout 单位秒
# r_timeout = requests.get('http://www.baidu.com', timeout=1)
# #发送带参数的请求.
# payload = {'key1': 'value1', 'key2': 'value2'}
# r_params = requests.get("https://www.baidu.com/", params=payload)
# #定制请求头
# url = 'https://www.baidu.com/s?wd=python'
# headers = {
#         'Content-Type': 'text/html;charset=utf-8',
#         'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
#     }
# r_headers = requests.get(url,headers=headers)

# requests.post()用法与requests.get()完全一致，特殊的是requests.post()有一个data参数，用来存放请求体数据
# 以form形式发送post请求
# import requests
# import json
# payload = {'key1': 'value1','key2': 'value2'}
# r_key = requests.post("http://www.baidu.com", data=payload)
# #以json形式发送post请求
# url = 'http://www.baidu.com'
# payload = {'key1': 'value1', 'key2': 'value2'}
# r_json = requests.post(url, data=json.dumps(payload))

# import requests
# response = requests.get("https://www.baidu.com") #发送get请求
# print(response.status_code)  # 获取响应状态码
# print(response.url)  # 获取url地址
# print(response.text)  # 获取文本
# print(response.content)  # 获取二进制流
# print(response.headers)  # 获取页面请求头信息
# print(response.history)  # 上一次跳转的地址
# print(response.cookies)  # # 获取cookies信息
# print(response.cookies.get_dict())  # 获取cookies信息转换成字典
# print(response.cookies.items())  # 获取cookies信息转换成字典
# print(response.encoding)  # 字符编码
# print(response.elapsed)  # 访问时间

import requests
#请求信息
url_login = "https://oauthuat.utcook.com/uaa/oauth/login"  # 开发者中心登录接口
login_header = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
                "Content-Type": "application/x-www-form-urlencoded"}
data = {"username":"jiangman","password":"jJ1234567","grant_type":"password"}
#发送post请求
requests_login = requests.post(url_login, data,headers = login_header)
# print(requests_login.status_code)#返回状态码
# print(requests_login.json())#返回值

# 根据登返回的数据，设置后续接口header
if requests_login.status_code == 200 and "access_token" in requests_login.json():
    login_header = {}
    login_header["Authorization"] = requests_login.json()["token_type"] + " " + requests_login.json()["access_token"]
    login_header = login_header
    print("登录接口调用成功")
else:
    login_header = None
    print("登录接口调用失败，错误信息为：{}".format(requests_login.text))

if  login_header != None:
    url_get = "https://mobiledev.utcook.com/user/user/curUser"  # 获取用户登录信息
    #发送get请求
    requests_get = requests.get(url_get, headers = login_header)
    if requests_get.status_code ==200:#判断，当返回码为200，打印返回json
        print(requests_get.json())
    else:
        print("接口调用失败，返回信息为：{}".format(requests_get.text))
else:
    pass





# 重写TestCase的setUp() tearDown()方法：在每个测试方法执行前以及执行后各执行一次
# def setUp(self):
#     print("do something before test : prepare environment")
# def tearDown(self):
#     print("do something after test : clean up ")
#
# import unittest
#
# class TestUnit(unittest.TestCase):
#     #编写测试用例
#     def test_case1(self):
#         print("case1")
#     def test_case2(self):
#         print("case2")
# class TestUnit2(unittest.TestCase):
#     #编写测试用例
#     def test_case3(self):
#         print("case3")
#     def test_case4(self):
#         print("case4")
# if __name__ == "__main__":
#     loader = unittest.TestLoader()  # 创建测试加载器
#     suite = unittest.TestSuite()  # 创建测试包
#     # 该方法是添加该类下的一个测试用例
#     suite.addTest(TestUnit("test_case2"))
#     # 该方法添加该类下的所有测试用例；
#     suite.addTest(loader.loadTestsFromTestCase(TestUnit2))#加载整个测试类
#     import time
#     import HTMLTestRunnerNew
#     localtime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())  # 获取当前时间
#     with open(localtime + ".html", "wb+") as file:
#         runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                                   title="测试报告",
#                                                   description="测试用",
#                                                   tester="JM")
#         runner.run(suite)


# import ddt
# import unittest
# @ddt.ddt
# class MyCase(unittest.TestCase):
#     @ddt.data(1,2)  #运行2 次
#     def testa(self,value):
#         print(value)
#
#     @ddt.data([1,2]) #运行1 次
#     def testb(self,value):
#         print(value)
#
#     @ddt.data([1,2],[3,4]) #不加unpack 会报错
#     def testc(self,a,b):
#         self.assertNotEqual(a,b)
#
#     @ddt.data([1,2],[3,4]) #运行2 次
#     @ddt.unpack
#     def testd(self,a,b):
#         self.assertNotEqual(a,b)
#
# if __name__ == '__main__':
#     unittest.main()