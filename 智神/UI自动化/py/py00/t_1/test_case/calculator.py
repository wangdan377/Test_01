#!usr/bin/env python3
#-*- coding:utf-8 _*-
"""
@author:shilei
@file: calculator.py
@time: 2020/08/18

__author__ = "lei.shi@ximalaya.com"
"""

class Calculator():
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    #加法
    def add(self):
        return self.a + self.b

    #减法
    def sub(self):
        return self.a - self.b

    #乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b
if __name__ == '__main__':
    cal = Calculator(3,2)
    print(cal.add())
    print(cal.sub())
    print(cal.mul())
    print(cal.div())