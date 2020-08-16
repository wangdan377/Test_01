"""import unittest
from parameterized import parameterized
class Mytest(unittest.TestCase):
    @parameterized.expand([(3,1),(1,0),(2,4)])
    def test_values(self,first,second):
        self.assertTrue(first > second)
unittest.main(verbosity=2)"""

"""import unittest
from parameterized import parameterized

class MyTest(unittest.TestCase):
    @parameterized.expand([(3,1), (-1,0), (1.5,1.0)])
    def test_values(self, first, second):
        self.assertTrue(first > second)

unittest.main(verbosity=2)"""
import requests
import json

login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
           "Content-Type": "application/x-www-form-urlencoded"}
login_data = {"username": "developer_app_admin", "password": "Ut123456", "grant_type": "password",
              "scope": "read"}
response = requests.post(url=login_url, headers=headers, data=login_data)
access_token = response.json()["access_token"]
Authorization_value = "bearer " + access_token
global headers1
global headers2
global headers3
headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
headers2 = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": Authorization_value}
headers3 = {"Authorization": Authorization_value}

"""import requests
import pytest
#定义一个参数化需要的数据，必须是列表！
appId1 = [{'appId':'a6'},{'appId':'a7'},{'appId':'a8'}]

#类似于java上的注解，标记数据源，将数据源给username
@pytest.fixture(params=appId1)
def username(request):
    return request.param
#类名
class Test_no():
    #方法名，传的参数就是，数据给了装饰器，作为参数给了下面的方法
    def test_learn(self,appId1):
        url="https://mobileuat.utcook.com/settle/appInfo/bindApp"
        body={'appId':'111'}

        # 数据源是list，使用下标取值，并赋值给body
        body["appId"] = appId1[0]
        # 数据源是Dictionary，使用key取值，并赋值给body
        # body["appId1"] = appId1["appId1"]
        # body["password"] = username["password"]
        # 调用post方法，传入url,body两个参数
        r1= requests.post(url=url,headers=headers2,json=body)
        # 最后输出响应结果
        print(r1.text)
        # 增加断言
        # assert r1.json()["message"] == "操作成功"""

"""import requests
import pytest
#定义一个参数化需要的数据，必须是列表！
#undata1 = [['张飞9','111111'],['张飞10','222222'],['张飞11','333333'],['张飞12','444444']]
undata1 = [{'username':'嘘嘘01','password':'111111'},{'username':'嘘嘘02','password':'111111'},{'username':'嘘嘘03','password':'111111'}]

#类似于java上的注解，标记数据源，将数据源给username
@pytest.fixture(params=undata1)
def username(request):
    return request.param

#类名
class Test_no():
    #方法名，传的参数就是，数据给了装饰器，作为参数给了下面的方法
    def test_learn(self,username):
        url="http://localhost:8080/admin/register"
        body={
  "email": "string",
  "icon": "string",
  "nickName": "string",
  "note": "string",
  "password": "12112",
  "username": "11212"
}
        # 数据源是list，使用下标取值，并赋值给body
        #body["username"] = username[0]
        #body["password"] = username[1]

        ## 数据源是Dictionary，使用key取值，并赋值给body
        body["username"]=username["username"]
        body["password"] = username["password"]
        # 调用post方法，传入url,body两个参数
        r1= requests.post(url=url,json=body)
        # 最后输出响应结果
        print(r1.text)
        # 增加断言
        assert r1.json()["message"] == "操作成功"""
import unittest
from ddt import ddt,data,unpack

@ddt
class MyTest(unittest.TestCase):
    @data((3, 1), (-1, 0), (1.2, 1.0))
    @unpack
    def test_values(self, first, second):
        self.assertTrue(first > second)

unittest.main(verbosity=2)