# coding:utf-8
import unittest
class xsep(unittest.TestCase):
    '''
    每次执行函数方法时，必须先执行一次setup（），执行完一个函数方法后，必须再执行一次teardown（）函数
    '''
    def setUp(self):
        print("前置条件")
    def tearDown(self):
        print("结束测试条件")
    def testadd(self):
        print('1+1=',1+1)
    def testsub2(self):
        print('3-2=',3-2)
if __name__ == '__main__':
    unittest.mian()

class xsep(unittest.TestCase):
    '''
    #setup()在所有用例执行之前只执行一次，和teardown（）函数在所有用例执行之后只执行一次
    '''
    @classmethod
    def setUpClass(self):
        print("前置条件")

    @classmethod
    def tearDownClass(self):
        print("结束测试条件")
    def testadd(self):
        print('1+1=',1+1)
    def testsub2(self):
        print('3-2=',3-2)
if __name__ == '__main__':
    unittest.mian()







