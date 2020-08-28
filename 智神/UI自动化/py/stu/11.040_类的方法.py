"""class Animal(object):
    is_alive = True
    health = 'good'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal('lili',18)
print(Animal.health)
print(hippo)
print(hippo.name,hippo.age)
hippo.description()"""
"""这个类除了初始化还有两个方法：向购物车里添加的add_item和从购物车里移出商品的remove_item
用这个类创建一个shoppingcart类的对象my_cart.初始化时填的customer_name的值请随意输入。
然后使用add_item方法向这个购物车随意添加一个商品。
传入参数product表示商品名，price表示价格"""
"""class ShoppingCart(object):
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}
    def add_item(self,product,price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print('{}加入购物车'.format(product))
        else:
            print('{}本来就在购物车里'.format(product))
    def remove_item(self,product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print('{}被移出购物车'.format(product))
        else:
            print('{}不在购物车里'.format(product))

customers = ShoppingCart("衣服")
print(customers.customer_name)
customers.add_item("skrt",100)
customers.remove_item("skrt")"""
# 同一个类中的不同方法中的变量调用：
# 类不同方法函数的调用是通过直接是self.变量名
"""class A():
    def a_add_b(self):
        a = 10
        b = 20
        self.s = a + b
        self.s1 = a * b

        return self.s, self.s1

    def c_add_ab(self):
        c = 30
        s = c + self.s
        s2 = c + self.s1
        print(s)
        print(s2)


t = A()
t.a_add_b()
t.c_add_ab()"""




# 不同函数中的变量调用：
# 不同函数中则是先调用函数并赋值给一个变量f, 并通过f[]调用，因为函数a_add_b()返回的是一个元组。
def a_add_b():
    a = 10
    b = 20
    s = a + b
    s1 = a * b
    return s, s1

print(a_add_b())     #打印出第一个函数的值


def c_add_ab():
    f = a_add_b()
    c = 30
    m = c + f[0]
    print(m)

# a_add_b()
c_add_ab()
