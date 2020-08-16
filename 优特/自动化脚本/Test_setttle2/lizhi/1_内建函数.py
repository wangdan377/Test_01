'''
#内建函数
print('abc'.capitalize())  #把字符串得第一个字母大写
str1= "abc"
print(str1.center(6,"1"))  #str.center(width,fillchar)  fillchar为填充字符，只能一个字符
str2 = "hello python world"
print(str2.count("o",5,30))      #"str.count(sub, start=0,end=len(string) )

str3 = 'name.py'
suffix = '.py'
print(str3.endswith(str3, 0, 20)) # True

str1 = 'I\'m\tfine,thank you! '
print(str1) # I'm   fine,thank you!
print(str1.expandtabs(10)) # I'm       fine,thank you!

str1 = '小明,小红,小花 '
str2 = '小花'
str3 = '小张'
print(str1.find(str2, 2), str1.find(str3, 2)) # 6 -1  str1包含str2
print(str2.find(str1, 1))  #st2不包含str1  所以为-1

str1 = input('请输入一个字符串:')
print(str1.islower())

str1 = input('请输入一个字符串:')
print(str1.isnumeric())

str1 = input('请输入一个字符串:')
print(str1.istitle())

str1 = ' 1'
str2 = 'abc'
print(str1.join(str2))  # a b c
'''



'''
区别:isdigit() isdecimal() isnumeric()
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
'''
"""
"""
name_score= dict(A=77,B=69,C=88,D=99,E=65,F=61)
'''
假设一个班级没有重名的学生，一个字典记录了班级的学生姓名和分数,找出最高分和最低分
'''
min_score = max(zip(name_score.values(),name_score.keys()))
max_score = zip(name_score.values(),name_score.keys())
max_score = min(zip(name_score.values(),name_score.keys()))
print(max_score,min_score)