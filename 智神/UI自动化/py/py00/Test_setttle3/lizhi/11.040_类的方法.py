"""向Animal类添加一个desciption方法，在这个方法的方法体内使用两个print语句
把当前对象的name和age打印到屏幕上
接着用Animal类创建一个对象hippo，这个对象的name和age请你自己随意指定
然后在创建出来的对象上调用description方法
注意这个方法也要加上默认的一个参数self"""
"""class Animal(object):
    is_alive = True
    def __init__(self,name,age):
        self.names = name
        self.ages = age
    def description(self):
        print('名字叫什么'+self.names)
        print('年龄呢？'+str(self.ages))
hippo = Animal('lili',18)   #创建类的对象hippo,
print(hippo.names,str(hippo.ages))
hippo.description()"""
class Animal(object):
    is_alive = True
    health = 'good'   #添加一个类变量，然后用三个对象把类变量打印出来
    def __init__(self,name,age):
        self.names = name
        self.ages = age
    def description(self):
        print('名字叫什么'+self.names)  #把当前对象的name和age打印到屏幕上
        print('年龄呢？'+str(self.ages))
hippo = Animal('lili',18)   #创建类的对象hippo    #用Animal类创建一个对象hippo    
sloth = Animal('paint',20)
ocelot = Animal('fruit',22)
print(hippo.names,str(hippo.ages))
hippo.description()  #调用description
# print(hippo.health)
# print(sloth.health)
# print(ocelot.health)
# print(Animal.health)


"""class Bus():
    def __init__(self,name,type,num):
        self.name = name
        self.type = type
        self.num = num
    def add1(self):
        print('需要添加多少油'+self.num)
    def run(self):
        print('可以跑1000公里')
bus = Bus('A品牌','公共汽车',500)
print(bus.name+'\n'+bus.type+'\n'+str(bus.num))"""

"""class Animal:
    #定义类的构造方法
    def __init__(self,lb):
        self.lb=lb
    #获取动物类别
    def getLB(self):
        return self.lb
class Dog(Animal):
    hungry = True
    def __init__(self):
        print("汪汪汪！")
    def eat(self,hungry=False):
        if(self.hungry):
            print("我要吃饭啦！")
            self.hungry=hungry
        else:
            print("我吃饱啦！")
实例化类
animal=Animal(lb="鸟类")
print(animal.getLB())

dog=Dog()
dog.eat()
dog.eat()"""


class ShoppingCart(object):
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}
    def add_item(self,product,price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print("{}加入购物车.".format(product))
        else:
            print("{}本来就在购物车里".format(product))
    def remove_item(self,product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print("{}被移除了购物车".format(product))
        else:
            print("{}不在购物车里".format(product))
# pro = ShoppingCart()
# pro.add_item('shirt',20)
# pro.add_remove_item()