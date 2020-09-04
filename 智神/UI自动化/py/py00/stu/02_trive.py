import unittest
import pymysql

def hotel_cost(nights):   #房价每天488元
    return nights * 488
# result = hotel_cost(2)
# print(result)

def train_cost(city):    #高铁费用
    if city == '上海':
        return 92.5
    elif city == '南京':
        return 117.5
    elif city == '苏州':
        return 111.5
    elif city == '西安':
        return 653.5
# result1 = train_cost('上海')
# print(result1)

def rent_cat_cost(days):   #租车费用
    if 0 <=days <=3:
        return days * 78
    elif 3 < days <= 7:
        return days *58
    elif days >7:
        return days *11
# result2 = rent_cat_cost(5)
# print(result2)

def trip_cost(city,days):    #旅行总费用
    city = train_cost(city)  #高铁费用
    days = hotel_cost(2) +rent_cat_cost(2)   #旅馆+租车费用
    return city*2+ days

qazw = trip_cost('上海',2)
print(qazw)