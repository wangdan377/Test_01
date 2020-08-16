'''
    目标完成登录业务层实现
'''

import unittest
from api.api_login import ApiLogin
# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    def test_login(self):
        # 暂时存放数据
        url = 'https://oauthuat.utcook.com/uaa/oauth/login'
        username = 'iot_owner_test'
        password = 'Ut123456'
        grant_type = 'password'
        scope = 'read'
        # 调用登录方法
        s = ApiLogin().api_post_login(url,username,password,grant_type,scope)
        # 调用使用
        print("查看响应结果： ",s.json())
        # 断言响应信息及状态码
        # if self.assertEqual("bearer",s.json()["token_type"]) :#前面是预期结果  后面是实际结果
        #     print("pass")
        # # 断言响应状态码
        # #     self.assertEqual(200,s.status_code)
        # else:
        #     print("error")

        self.assertEqual("bearer1", s.json()["token_type"],msg='跟实际不相符')
        self.assertEqual(200, s.status_code)

if __name__ == '__main__':
    unittest.main()
