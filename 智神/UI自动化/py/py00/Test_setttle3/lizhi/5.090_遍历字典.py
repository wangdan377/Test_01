#
#
# d = {"foo" : "bar","foo2":"bar2"}
# #用k遍历一个字典
# for s in d :   #key只是临时变量
#     print(d[s])  #打印出value
#     print(s)        #打印出key
#
# d = {"foo" : "bar","foo2":"bar2"}
# # 用key,value遍历一个字典
# for m,n in d.items() :   #key只是临时变量
#     print(m)
#     print(n)
#
webster = {
        "Aardvard" : "A star of a popular childrend's cartoon show.",
        "Baa" : "The sound a goat makes.",
        "Carpet" : "Goes on the floor.",
        "Dab" : "A small amount."
    }
#遍历应打印出这个字典的所有值
for key in webster :
    print(webster[key])

#用key，value遍历一个字典
for key1,values1 in webster.items():
    print(values1)
    print(key1)




