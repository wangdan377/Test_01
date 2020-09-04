'''
def using_control_once():
    if 2>1:
        return "Success #1"
def using_control_again():
    if 4<19:
        return "Success #2"
print(using_control_once())
print(using_control_again())
'''
'''
if 8>9:
    print("我会执行")
else:
    print("我不会执行")
'''

'''def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:
        return -1
    else:
        return 0
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))'''
def grande_converter(grade):
    if grade>90:
        return "优秀"
    elif grade>=80 and grade<89:
        return "良好"
    elif grade >= 70 and grade < 79:
        return "尚可"
    elif grade>=60 and grade<69:
        return "待改进"
    else:
        return "不及格"
print(grande_converter(91))
print(grande_converter(80))
print(grande_converter(60))
print(grande_converter(59))



