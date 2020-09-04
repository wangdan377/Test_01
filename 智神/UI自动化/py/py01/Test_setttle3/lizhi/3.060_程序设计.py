original = input("请输入一个英文单词")
print(original)
# original = "Pig Lagin"
def cha():
    if len(original) >0 and original.isalpha() :
        print("是字母")
    elif original.isdigit():
        print('只含数字')
    elif original.isalnum():
        print('字母或者数字')

    else :
        print("输入的单词不合法")

cha()

original1 = "Pig Lagin"
original2 = original1.lower()[0:2]
original3 = original1.lower()[2:]
original4 = original3 + original2
print(original4)

