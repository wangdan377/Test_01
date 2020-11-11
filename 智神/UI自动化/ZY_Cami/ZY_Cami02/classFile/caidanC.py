# -*- coding: utf-8 -*-
from classFile.caidanA import methorA
from classFile.caidanB import methorB
class methorC(methorB):
    def __init__(self):
        methorB.__init__(self)#直接继承B类文件的构造方法
    def threes(self):
        # print(self.age,'姓名：',self.name,'地址：',self.home)  #因为B类没有继承A类的初始化函数  所以没办法使用self.age属性
        # print('姓名：',self.name,'地址：',self.home)
        print('姓名：', self.twos(), '地址：', self.home)

    # def ones(self): #虽然是继承但是方法可以重写  不明白啥意思就取消注释  然后运行一下
    #     age = 18
    #     return age
if __name__ == '__main__':
    cai3 = methorC()
    cai3.threes()
    print(cai3.twos())  #继承之后可以直接使用父类 （B文件的类）的方法
    print(cai3.ones())   #因为B类继承A类  所以可以调用A的方法   但是不能调用A类的属性
