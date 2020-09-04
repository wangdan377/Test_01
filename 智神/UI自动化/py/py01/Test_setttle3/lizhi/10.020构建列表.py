
# 语法：表达式for 变量 in 列表 if条件
"""my_list = range(51)
print(my_list)

evens_to_50 = [i for i in range(51) if i %2 ==0]
print(evens_to_50)

list_1_10 = [x**2 for x in range(1,11)]   #列表推导式
print(list_1_10)

a = [[1,2,3],[4,5,6],[7,8,9]]  #多种嵌套
a = [j**2 for i in a  for j in i if j %2==0 ]
print(a)"""
new_list = [x for x in range(1,6)]
print(new_list)

new_list = [x*2 for x in range(1,6)]  #列表中数字两倍
print(new_list)

new_list = [x*2 for x in range(1,6) if(x*2)%3 ==0]  #能被3整除
print(new_list)

a = [[1,2,3],[4,5,6],[7,8,9]]  #多种嵌套
a = [j**2 for i in a  for j in i if j %2==0 ]
print(a)
"""#想要得到多重嵌套的list中一重嵌套中list长度大于1的list中的数为2的倍数的平方组成的list
b = [[1,2,3],[4,5,6],[7,8,9]]
b = [j**2 for i in a if len(i)>1 for j in i if j%2 == 0]
print(b)"""


c = [i**2 for i in range(1,11) if i%2==0] #1-11所有偶数的平方
print(c)

#在列表推导中最前面的表达式里不一定要包括变量
# 而最后的if限制条件会对中间每个循环结果得到的x都做一次过滤
d = ['C' for x in range(5) if x<3]
print(d)

cules_by_four = [i**3 for i in range(1,10) if i%4 ==0]
print(cules_by_four)