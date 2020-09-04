#!usr/bin/env python3
#-*- coding:utf-8 _*-
"""
@author:shilei
@file: 1.py
@time: 2020/08/24

__author__ = "lei.shi@ximalaya.com"
"""
import os
import sys

def test_add1():
    print(os.sep + sys._getframe().f_code.co_name+'.png')
test_add1()
