"""
def square(n):
    '''
    计算一个数字的平方
    :param n
    :return 返回这个数字的平方值
    '''
    squared = n**2
    print("{}的平方是{}".format(n,squared))
    return squared
square(10)

def square(n):
    '''
        计算一个数字的平方
        :param n
        :return 返回这个数字的平方值
        '''
    squared = n**2
    return squared
my_number_squared = square(10)
print(my_number_squared)

def square(n):
    '''
        计算一个数字的平方
        :param n
        :return 返回这个数字的平方值
        '''
    squared = n**2
    return squared
my_number_squared = square(10)
print(square(10))

"""

# x = input("请输入数字： ")
# x = int(x)
# print(x)
def number(n):
    '''
    :param n
    :return 返回这个数的立方
    '''
    numberd = n**3
    n = int(n)
    if n %3 == 0:
        print("{}的立方等于{}".format(n,numberd))
    else:
        print("False")
    return numberd
number(10)

'''
x1 = input("请输入数字：")
x1 = int(x1)
if x1 % 3 == 0:
    print("%d能被3整除" %(x1))
else:
    print("%d 不被3整除" %(x1))
'''
