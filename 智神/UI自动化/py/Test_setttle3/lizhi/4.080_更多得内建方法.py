# coding = utf-8
"""def biggest_number(*args):
    '''

    :param args:
    :return: 返回最大值
    '''
    print(max(args))
    return max(args)
biggest_number(1,2,-1,-6,9)

def biggest_number1(*args):
    '''

        :param args:
        :return: 返回最小值
        '''
    print(min(args))
    return min(args)
biggest_number1(1,2,-1,-6,9)

def biggest_number2(arg):
    '''

        :param args:
        :return: 返回绝对值
        '''
    print(abs(arg))
    return abs(arg)
biggest_number2(1)

print(type(42))
print(type(4.2))
print(type('面包'))"""

from pprint import pprint as pp
'''
python类对象的特殊方法
'''




"""class A(object):
    def __init__(self):
        self.PropertyA = 1
class B(object):
    def __init__(self):
        self.PropertyB =2
    def b_method(self):
        pass

NewA =A.__class__('NewA',(A,B),{"NewProperty": 'xxxxx'})
new_a = NewA()
print(dir(new_a)[:3])
print(new_a.__class__.__name__)"""

"""def shut_down(s):
    '''
    定义一个方法shut_down,这个方法接受一个掺入参数s
    :param s:
    :return: 返回yes ,关闭执行中。返回no,已取消关闭操作。否则 对不起，无法执行
    '''
    if s =='yes':
        print("关闭执行中")
    elif s == 'no':
        print("已取消关闭操作")
    else:
        print("对不起，无法执行")
shut_down("yes")"""



def isOdd():
     x = eval(input("请输入一个数，是奇数数输出true，不是就false\n"))
     if(type(x)==int):
         if(x%2!=0):
          print("true")
         elif(x%2==0):
           print("false")
     else:
        print("请输入一个整数")
isOdd()

















