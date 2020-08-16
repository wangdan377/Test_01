# animal = ['cat','nose','leg']
# animals = sorted(animal)
# print(animals)
'''
sort方式是列表上用点调用，而sorted方法是把列表作为参数传给他来调用。
点号调用说明这个方法是列表专属，而把列表作为参数传给sorted来调用则说明
1，sorted是一个内建方法
2，sorted能接受得数据类型很可能不仅仅是列表
'''
# animals= ['cat','nose','leg']
# animals.sort()
# # for animal in animals :
# #     print(animal)
# print(animals)

# animals1 = {"height":"180","age":"18"}   #sort只对列表有用，所以这里是有问题得
# animals1.sort()
# print(animals1)

# animals1 = {"height":"180","age":"18"}   # 列表作为参数传给sorted来调用
# animals2 = sorted(animals1)
# print(animals2)


'''
对列表start_list做遍历，并把其中每个元素得二次方作为新的元素追加进列表square_list,
并对square_list进行排序后打印
'''

'''
start_list = [5,3,2,1,4]   #直接调用
square_list = [7,8]
for vor in start_list:
    print(vor**2)
    vor1=vor**2
    square_list.append(vor1)
print(square_list)
square_list.sort()
print(square_list)
square_list.reverse()
print(square_list)
'''




start_list = [5,3,2,1,4]
square_list = [7,8]
for vor in start_list:
    print(vor**2)
    vor1=vor**2
    # vor1 = ([vor1])
    square_list.append(vor1)
#     square_list2=square_list.extend([vor1])
print(square_list)
# square.list.extend([i ** 2 for i in list])
  # square_list.extend([i ** 2 for i in start_list])
  #extend函数添加得对象必须是可迭代对象，字符串和列表都是可迭代对象，但是数字不是，转成列表才能添加进去
# print(square_list2)
# square_list1 = sorted(square_list)   #列表作为参数传递给sorted来调用
# print(square_list1)




# l = [4,5,6]
# l_tuple = ('sdf','dfg')
# l_set = {'tyr','ert'}
# l_list = [1,2,3]
# l.extend(l_tuple)
# print("新列表：",l)





