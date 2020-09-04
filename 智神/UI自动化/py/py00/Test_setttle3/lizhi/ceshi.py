"""# coding:utf-8
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

"""
"""def print_list(x):
    '''把x的元素一个一个print出来
    然后把下面的n作为参数传给这个方法'''
    for i in x:
        print(i)
n = [3,5,7]
# print_list(n)
print(n)
"""
"""def double_list(x):
    '''每个元素乘以2打印出来'''
    for i in x:
        print(i*2)
n = [3,5,7]
double_list(n)
# print(n)"""

"""def list_function (x):
    '''方法里返回x的第二个元素'''
    return x[1]
n = [3,5,7]
print(list_function(n))
"""
"""def my_function(x):
    '''在下划线处填入一个列表，值为【0，1，2】
    必须使用range来生成这个列表'''
    y = []
    for i in range(0, len(x)):
        y.append(x[i])
    return y
print(my_function((1,2,3)))"""

"""list = [1,2,3]
# '''通过in遍历，简单的遍历列表，单不能再遍历的同时进行修改'''
# for item in list:
#     print(item)

for i in range(len(list)):
    '''通过下标来遍历，在遍历的同时对列表内元素做修改'''
    print(list[])i"""

"""#数组之和
a = []                            #定义一个数组，保存求和的所有整数
n = input("请输入求和的数值总数:")  #输入求和的整数个数，保存在变量n中
for i in range(0,len(n)):           #用for循环，控制输入所有的求和整数
    m = input('请输入一个整数：')    #输入所有的求和整数，保存在数组中
    a.append(int(m))                
print('数组元素为：')

for i in a:                        #输出所有求和的整数
    print(i,end='')
print()
s=sum(a)                            #调用sum函数，计算所有整数的和
print('各数组元素的和为：',s)"""     #输出计算得到的所有整数和

"""def total(numbers):
    result  = 0
    for i in sum(range(0,len(numbers))):
        print(n)
n = [3,5,7]
s = sum(n)
print(s)
print(total(n))"""


"""number = 5
def my_function(x):
    '''这个方法返回得值等于传入参数+3'''
    return x+3
print(my_function(number))"""
"""m = 5
n = 15
def add_function(m,n):
    '''接受两个参数，并返回两个参数之和'''
    return m+n
print(add_function(m,n))

n = 'hello'
s = 'word'
def string_function(n):
    '''接受一个参数s,返回一个字符串.
    这个字符串等于在s后面加上word这个词,中间不要空格'''
    return n+s
print(string_function(n))
"""


# def list_function(x):
#     '''返回第二个元素'''
#     return x
# n = [3,5,7]
# print(list_function(n))

"""def list_extender(lst):
     '''给列表后面追加一个元素'''
     lst = lst.append(2)
     return n
n = [3,5,7]
print(list_extender(n))
"""

"""def test(n):   #每个元素乘以5
     x = [i*5 for i in n]
     return x
n = [3,5,7]
print(test(n))"""
