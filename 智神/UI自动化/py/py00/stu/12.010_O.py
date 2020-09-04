import os
# rjust()方法, 它可以将字符串靠右, 并在左边填充空格
"""for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end='...')
    print(repr(x*x*x).rjust(10))

for x in range(1, 11):
    # print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
    print('{0:5d} {1:10d} {2:4d}'.format(x, x * x, x * x * x))"""
# f.write字符串写入到一个文件
"""f = open("1.txt", "w")
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f.close()
"""

"""
#f.read()打开文件
f = open('1.txt',"r")
str = f.read()
print(str)
f.close()
# f.readline()读取单独的一行
f = open('1.txt',"r")
str = f.readline()
print(str)
f.close()
# f.readlines()将返回该文件中包含的所有行
f = open('1.txt',"r")
str = f.readlines()
print(str)
f.close()
# 迭代一个文件对象然后读取每行
f = open('1.txt',"r")
for line in f:
    print(line,end='')

f.close()"""

#写入带有不是字符串的，要转换为字符串
"""f = open('1.txt','w')
value = ('www.baidu.com',14)
s = str(value)
f.write(s)
f.close()


f = open('1.txt','r')
str = f.read()
print(str)
f.close()
"""

# with open('1.txt','r') as f:
#     read_data = f.read()
# f.closed

# 文件写入内容
"""my_list = [i**2for i in range(1,11)]   #1-10的平方列表推导式
f = open("1.txt","w")
for item in my_list:
    f.write(str(item)+"\n")
f.close()
# 读取文件
f = open('1.txt','r')
str = f.read()
print(str)
f.close()"""

my_life = [1,2,3]
my_life = str(my_life)
f = open('1.txt','r+')
str = f.read()
f.close()



