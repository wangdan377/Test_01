'''
def coupon(original_price):
    new_price = original_price-int(original_price/80)*20
    print("选择满减优惠后得价格为：{}".format(new_price))
    return new_price
coupon(100)
'''


"""def coupon(original_price):
    '''
    满80减20
    ：param:original_price 原价
    ：return:折后价
    '''
    new_price = original_price-int(original_price/80)*20
    print("选择满减优惠后的价格为：{}" .format(new_price))


original_price = 80
coupon(original_price)  #直接调用这个函数


def discount(original_price):
    '''
    params:参数为original_price
    return:返回 打折八折
    '''
    new_price = original_price*0.8
    print("打八折后的价格为：{}".format(new_price))
    return new_price


original_price = 100
discount(original_price)"""


"""def cook(food):
    '''
    params:food,参数为egg
    return: 返回’番茄加鸡蛋‘
    '''

    print("返回的信息为{}".format(food))
    return food
food = "tomato\negg"
cook(food) #调用哪个方法，使用什么参数调用这个方法。执行方法体里面的语句
"""
# 用数字10作为参数调用计算平方的方法（就是把10放到调用时的括号里）
"""def square(n):
    '''
    计算一个数字的平方
    param n
    return:这个数字的平方值
    '''
    squared = n**2
    # print("{}的平方时{}".format(n,squared))
    return squared
my_squard = square(11)   #把值返回存到变量里
print(my_squard)
print(square(10))   #直接用了返回值，没有保存在变量里"""

"""def method_1():
    return 5
    '''ruturn和print的区别
    return 用来在方法体内返回。print用来向屏幕上输出内容，完全不同。
    print并没有返回功能。如果你看到一个方法里没有写return，
    那是因为没写return的方法会在执行完方法体后自动返回一个空值'''
    print('我不会被执行')

a = method_1()"""


