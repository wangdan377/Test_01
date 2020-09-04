"""#列表的人名一次打印出来
names = ['Adam','Alex','Maeiah','Martine','Columbus']
for n1 in names :
    print(n1)"""
"""# 在for 循环中的 循环体 部分，可以包含很多内容，比如把条件分支放进去
numbers = [1,3,4,7]     #这个例子中，只会print出列表中比6大的元素
for number in numbers:
    if number > 6:
        print(number)"""
"""#所有关键字
import keyword
print(keyword.kwlist)"""
"""#定义一个列表a，其中包含一些数字。遍历并打印出其中能被2整除的数字
a =[1,2,3,4,5,6,7,8,9,10]
for x in a :
    if x %2 == 0:
        print(x)"""
"""# 打印出1-100的自然数，但是对其中的一些数字要把它替换成一下单词：
#当这个数字是3的倍数时，替换成Fizz,当这个数字是5的倍数时，替换成Buzz,
# 当它是3的倍数又是5的倍数时替换成FizzBuzz
# for i in range(2):
#     print(' '.join(["fizz"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or str(x) for x in range(1, 101)]))
# 第二种方法
for i in range(1,101):
    if i % 3 ==0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    elif i %3 and i %5 == 0:
        print('Fizz','Buzz')
    else:
        print(i)
"""