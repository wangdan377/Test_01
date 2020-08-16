
"""number = 5
def my_function(x):
    '''
    返回的值等于传入参数*3
    :param x: 参数x
    :return: 返回值相乘
    '''
    return x * 3
print(my_function(number))"""

"""#接受两个参数，并返回两个参数之和
m = 5
n = 13
def add_function(m,n):
    return m + n
print(add_function(m,n))
"""
"""#定义一个参数，返回一个字符串
n = "hello"
def string_function(s):
    return s + "word"
print(string_function(n))"""

"""#列表做参数和其它类型做参数是一样的
def list_function(x):
    return x
n =[1,2,3]  #n =(1,2,3)
print(list_function(n))
"""
def my_function(x):
    y = []
    for i in range(0,len(x)):
        y.append(x[i])
    return y
print(my_function((1,2,3)))

# for item in list:
#     print(item)



