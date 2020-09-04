"""class Customer(object):
    def __init__(self,customer_id):
        self.customer_id = customer_id
    def display_cart(self):
        print("购物车中有以下商品：xxxxxx")
class ReturningCustomer(Customer):
    def display_order_history(self):
        print("历史订单有：xxxxx")
monty_python = ReturningCustomer("ID:12345")
monty_python.display_cart()
monty_python.display_order_history()"""
#继承
"""class Shape(object):
    def __init__(self,number_of_sides):
        self.number_of_sides = number_of_sides
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3"""
#方法重写override
"""老板向员工打招呼和员工向老板或员工之间打招呼可能方式完全不同。这里我们在BOSS类里并没有
选择创建一个新的向下属打招呼的方法，而是直接重写了打招呼用的greet方法。
于是，在最后调用这个方法时，python发现这个BOSS类里有一个greet，相当于在子类里重新写了一遍父类里存在的方法
我们读子类代码时，心里可以想象，把父类里的各种属性定义和方法定义的代码复制粘贴到子类里面
形成了一个完整的子类。而有重复的方法或属性时，选择用子类里的定义的"""
"""class Employee(object):
    def __init__(self,name):
        self.name = name
    def greet(self,other):
        print("你好,%s" %other.name)
class BOSS(Employee):
    def greet(self,other):
        print("赶紧干活去,%s！" %other.name)
        
boss = BOSS("比尔")
emp = Employee("小明")
emp.greet(boss)
boss.greet(emp)"""
#任务3
#临时工继承员工类，临时工工资时薪40元，就散工资的方法就应该返回40乘以小时数
"""class Employee(object):
    def __init__(self,employee_name):
        self.employee_name = employee_name
class ParTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 100.00
emp = ParTimeEmployee("工资")
print(emp.calculate_wage(40))"""
#方法重写后想要想要访问父类方法
# super() 函数是用于调用父类(超类)的一个方法
"""class Base(object):
    def m(self):
        return "父类的方法调用结果"
class Derived(Base):
    def m(self):
        return super(Derived,self).m()+"子类的计算结果"
d = Derived()
print(d.m())"""

# 实例
class FooParent(object):
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
        print('Child bar function')
        print(self.parent)

fooChild = FooChild()
fooChild.bar('HelloWorld')
"""1,在临时工类里加上一个方法full_time_wage参数是self和hours
这个方法返回一个通过super调用calculate_wage方法，这个方法来自父类。参考例2
2，然后在代码最后另外起一行顶格写
创建临时工类的一个对象，变量名为milton.员工名字就叫"milton"
3.最后在milton上调用full_time_wage方法，并用print把结果打出来，调用时的工作时间为10h
答案为200"""
"""class Employee(object):
    def __init__(self,employee_name):
        self.employee_name = employee_name
    def calculate_wage(self,hours):
        self.hours = hours
        return hours*20.00
class ParTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self,hours):
        return super(ParTimeEmployee, self).calculate_wage(10)   #方法重写后想要访问父类
milton = ParTimeEmployee("milton")
print(milton.full_time_wage(10))   #调用的父类
print(milton.calculate_wage(10))    #调用的自己的函数
"""
