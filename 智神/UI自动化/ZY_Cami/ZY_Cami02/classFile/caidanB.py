# -*- coding: utf-8 -*-
from classFile.caidanA import methorA
class methorB(methorA):
    #继承A文件的类
    def __init__(self):
        #类实例化的时候  属性会自带  就像婴儿出生自带头发   头发是婴儿的属性
        self.name = self.twos()
        self.home = '山西'  #家属性
    def twos(self): #方法
        name = '王丹'
        return name
if __name__ == '__main__':
    cai2 = methorB()
    print(cai2.ones())