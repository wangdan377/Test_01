import math
# print(math.sqrt(13689))
import math
"""
def distance_from_zero(abs1):
    '''
如果传入参数类型是int或者float,返回传入参数的绝对值
    :param abs1:
    :return:传入参数类型，返回类型的绝对值
    '''
    if type(abs1) == int:
        print(abs(abs1))
    elif type(abs1) == float:
        print(abs(abs1))
    else:
        print("算不了")
    return abs1
distance_from_zero((1,2,))
"""
def hotel_cost(nights):
    '''
住几晚所需费用
    :param nights: 几晚
    :return: 返回所花费的费用
    '''
    hotel_cost1=input("请输入住几晚：")
    room = 488*nights
    print("住{}晚{}元".format(nights,room))
    return hotel_cost
hotel_cost(1)

def train_cost(city):
    city = input("请输入你要达到的城市：")
    '''
    如果选择“北京”，提示输入错误，如何继续运行代码呢
    :param city: 标识城市
    :return: 返回到达输入的城市所需的花费
    '''
    if city == "上海":
        print("到达{}所需花费92.5".format(city))
    elif city == "南京":
        print("到达{}所需花费117.5".format(city))
    elif city == "苏州":
        print("到达{}所需花费111.5".format(city))
    elif city == "上海":
        print("到达{}所需花费653.5".format(city))
    else:
        print('请重新输入')
    return city
train_cost('上海')

def rent_cat_cost(days):
    '''
    每天租车的价格是78元每天
    如果你租超过7天可以优惠67元
    如果你租超过3天可以优惠20元
    只能同事享受一种优惠方案，也就是不可以叠加
    :param days:
    :return:返回租车的费用
    '''
    days = int(input("请输入租车天数:"))
    days1 = 78
    days3 = days*78 -20
    days7 = days*78 - 67
    if days <= 3:
        print("如果租车{}天的价格是{}元".format(days,days1))
    elif days>3 or days<=7:
        print("如果租车{}天的价格是{}元".format(days,days3))
    elif days>7 :
        print("如果租车{}天的价格是{}元".format(days,days7))
    return days
rent_cat_cost(1)

def trip_cost(city,days):
    '''
    计算旅行总花费
    :param city: 高铁费用
    :param days: 住宿费用
    :return: 总费用=车费用+住宿费用+高铁费用
    '''
    hotel_cost(6)  #住几晚 night
    train_cost('上海') #目的地高铁费 city
    rent_cat_cost(6) #租车几天是多钱 days
    con =hotel_cost(6)+train_cost('上海')+rent_cat_cost(6)
    print("{} = {} + {} + {}".format(con,rent_cat_cost(6),hotel_cost('上海'),train_cost(6)))
    return trip_cost
trip_cost('上海',6)