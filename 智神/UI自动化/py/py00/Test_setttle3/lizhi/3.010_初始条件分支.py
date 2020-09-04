
'''def choice():
    print("请选择，左还是右？")
    answer = input("输入 左 或者 右 ：")
    if answer == '左' or answer == '右':
        print("你选择了左")
    elif answer == '右' or answer == '右边':
        print("你选择了右")
    else:
        print('你两个都没选，你决定再试一次')
        choice()
choice()'''



def chc():
    print("是true还是false")
    age = eval(input("请输入年龄："))
    if age >=18:
        print("可以出去玩耍")
    # elif age < 18 or age>0 :
    #     print("不可以出去玩")
    else:
        print("输入错误，请再次输入")
        chc()
chc()


