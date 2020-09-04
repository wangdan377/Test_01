# 任务1：创建一个Triangle三角形类。在init（）方法里接受参数self,angle1,angle2,angle3
# 这三个参数分别表示三个角的角度。然后在init方法里把这三个角度都设置成这个类的属性

# 任务2：接下来，在这个类里，创建一个类变量number_of_sides表示边的数量，并赋值为3
# 创建一个方法check_angles这个方法用来检查三个角的角度之和是否为180度，如果是，就返回True，否则返回False
# 注意在计算时，角度要用self.angle,self.angle2,self.angle3这样从类的属性里取出来

# 任务3：下一步，在类的外面顶格创建一个变量my_triangle并用Trangle类创建一个对象，把值付给这个变量。
# 创建对象时输入的三个角度为90，30，60
# 然后在屏幕上打出my_triangle.number_of_sides和my_triangle.check_angles()

# 任务4：最后一个任务，我们来创建一个等边三角形的类：Equilateral继承自三角形类Triangle
# 等边三角形的三个角都是60度，三条边的长度相等
# 1，创建一个等边三角形的类：Equilateral继承自三角形Triangle
# 2，在Equilateral类里创建一个类变量angle值为60
# 3，创建一个init()方法，接受参数是self。在方法体里把self.angle1,self.angle2和self.angle3都设置成等于self.angle
class Triangle(object):
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides=3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3>=180:
            return True
        if self.angle1+self.angle2+self.angle3<180:
            return False
my_triangle = Triangle(100,30,50)
"""print(my_triangle.angle1)
print(my_triangle.angle2)
print(my_triangle.angle3)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())"""
class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
my_triangles = Equilateral()
print(Equilateral.angle)

