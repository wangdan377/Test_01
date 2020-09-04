# 类之间的继承关系比较复杂
"""继承指的是类里可以用另一个类的属性和方法，继承的关系可以用“是一种”来理解
比如，熊猫是以中国熊，熊是一种哺乳动物。那么在熊猫这个类里可以用熊这个类的属性和方法
范例：宝马轿车是一种汽车，但是它不是一种拖拉机。所以他不能通过继承来使用拖拉机的属性和方法"""
"""class Coustomer(object):  #顾客
    def __init__(self,customer_id):
        self.customer_id = customer_id
    def display_cart(self):
        print("购物车中有一下商品：shirt")

class ReturningCustomer(Coustomer):  #回头客，
    def display_cart_history(self):
        print("历史订单有：shirt")
monty_python = ReturningCustomer("ID:12345")   #回头客继承了顾客，所以可以用顾客的属性和方法
monty_python.display_cart()
monty_python.display_cart_history()"""

#1到3行，我们创建了一个叫做Shape类，表示几何图形，初始化方法里指定了number_of_sides表示这个图形有几条边
# 2，在Triangle类里，写一个初始化方法，接受四个参数：self,side1,side2,side3
# 在这四个参数，第一个是初始化方法里的固定的self参数，后面的分别代表三角形的三条边
# 3，在初始化方法里，像这样：self.side1 = side1给各条边赋值

"""class Shape(object):
    def __init__(self,number_of_sides):
        self.number_of_sides = number_of_sides
        print("几何图形")
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        print("三角形")
ange = Shape("ID:12345")
anges = Triangle(1,2,3)
ange.number_of_sides
anges.side1
anges.side2
anges.side3"""

"""class Shape(object):
    def __init__(self,number_of_sides):
        self.number_of_sides = number_of_sides
        print("几何图形")
class Triangle(Shape):
    def __init__(self,number_of_sides,side1,side2,side3):
        super().__init__(number_of_sides)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3"""

"""class A:
    def add(self, x):
        y = x + 1
        print(y)
class B(A):
    def add(self, x):
        super().add(x)
b = B()
b.add(2)"""
'''在子类里面重写一遍父类里面的方法（方法重写）'''
"""class Employee(object):
    def __init__(self,name):
        self.name = name
    def greet(self,other):
        print("你好，%s" %other.name)
class BOSS(Employee):
    def greet(self,other):
        print("赶紧回去干活，%s!" %other.name)
boss = BOSS("比尔")
emp = Employee("小明")
emp.greet(boss)
boss.greet(emp)"""
"""class Employee(object):
    def __init__(self,employee_name):
        self.employee_name = employee_name
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):  #hours代表工作时间的小时数
        self.hours = hours
        return hours*40"""
'''方法重写后想要访问父类方法
有时候我们在写子类的一些方法时，一方面使用了重写，另一方面，又想要父类的同名方法提供的一些功能
这时我们可以用super来访问父类的方法'''
"""class Base(object):
    def m(self):
        return '父类的方法调用结果'
class Derived(Base):
    def m(self):
        return super(Derived,self).m()+'子类的计算结果'
d = Derived()
print(d.m())"""


"""class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')"""


"""class Employee(object):
    def __init__(self,employee_name):
        self.employee_name = employee_name

    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self,hours):
        return super(PartTimeEmployee,self).calculate_wage(hours)


milton = PartTimeEmployee('milton')
print(milton.full_time_wage(10))"""




