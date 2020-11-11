#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Public import Caplictily
from PO.Prime_Element import Prime_Page
from Public.Function import BaseFun
from Public.Wx_Pay import Wx_Config
from Public.Prime_Equipment import Prime_Buy_Equipment
from PO.login_element import Login_Page
from Public.Prime_Pay import Prime_Pay
from PO.Wx_Element import Wx_Page

# from Public.loged import Logger
# log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
class Prime_Equit_Members():
    '''是否 是会员'''
    def __init__(self,driver):
        self.driver = driver
        self.login = Login_Page(self.driver)  # 登录
        self.prime = Prime_Page(self.driver)  # prime
        self.fun = BaseFun(self.driver)
        self.login = Login_Page(self.driver)
        self.wx_pays = Wx_Config(self.driver)
        self.prime_pays = Prime_Pay(self.driver)
        self.wx = Wx_Page(self.driver)
        self.prime_buy_equipment = Prime_Buy_Equipment(self.driver)  # 购买设备
    def prime_equit_user(self):
        '''
        是会员，则续费-选择套餐-开通
        :return:
        '''
        try:
            self.prime.click_File_Renew()  # 立即续费
            self.prime.click_File_meal_03()  # 第3个套餐
            self.prime_buy_equipment.Prime_buy_Equipment_04()  # 购买多台设备
        except:
            time.sleep(2)
            self.prime.click_File_meal_03()     #套餐
            time.sleep(2)
            self.prime_buy_equipment.Prime_buy_Equipment_04()  # 购买多台设备

