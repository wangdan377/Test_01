import ddt,string
import unittest,datetime,random
# print(dir(ddt))

"""@ddt.ddt
class MyCase(unittest.TestCase):
    @ddt.data(1,2)  #运行2次
    def testa(self,a):
        print(a)

    @ddt.data([1,2]) #运行1次
    def testb(self,a):
        print(a)


    @ddt.data((1,2,5), (3,4,6))  # 不加unpack 会报错
    @ddt.unpack
    def testc(self, a,b,c):
        print(a,b,c)


    @ddt.data([1,2],[3,4]) #运行2次
    @ddt.unpack
    def testd(self,a,b):
        self.assertNotEqual(a,b)

if __name__ == '__main__':
    unittest.main()"""
"""import unittest
from ddt import ddt,data,file_data,unpack

import random
import string

a=random.randint(1,10)
print(a)

index = random.sample(range(0,3),1)
print(index)


print(random.random())
print(random.uniform(1, 10))

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,10)))
print(ran_str)

a=[]
for i in range(1,10):
    a.append(i)
@ddt
class demotest(unittest.TestCase):
    def setup(self):
        print("this is the setup")

    @data(*a)
    def testb(self,value):
        print(value)
        print("this is test b")

    @data([2,3],[4,5])
    def testa(self,value):
        print(value)
        print("this is test a")

    @data([2, 3], [4, 5])
    @unpack
    def testc(self, first,second):
        print(first)
        print(second)
        print("this is test c")



    def teardown(self):
        print("this is the down")

if __name__ == '__main__':
    unittest.main()"""

''.join(random.sample(string.ascii_letters + string.digits, 9))
# 1、random.sample(string.ascii_letters + string.digits, 9)表示随机抽取9位
# 2、str.join以某字符串，把抽取的字符连接起来
# str = "-"; seq = ("a", "b", "c");
# # 字符串序列
# print str.join( seq );
# 输出a-b-c
str = ''; seq=('a','b','c')
print(str.join(seq))

# ran_str = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,10)))
# print(ran_str)

s = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,3)))
print(s)

