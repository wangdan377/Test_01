#处理单个异常
"""name = [1,2,3]
try:
    name[1]       #code 处理语句
except IndexError as e:    #遇到报错执行下面的语句
    print(e)  """

#处理多个异常
"""name = [1, 2, 3]
data = {'a':'b'}
try:
    data['a']    #已经出现异常keyError,所以直接跳出来code,跳到keyError下去处理
    name[5]
except IndexError as e:   #超过索引报错
    print(e)
except KeyError as e:     #访问字典里不存在的键
    print(e)"""

# 写一个except,语法如下
"""name = [1, 2, 3]
data = {'a':'b'}
try:
    data['5']
    name[5]
except (IndexError,KeyError) as e:  #不管出现里面任何一种错误都用统一的处理方法
    print(e)"""
#Exception异常,捕获所有的异常
"""name = [1, 2, 3]
data = {'a':'b'}
try:
    name[5]
    # open('qigao,text','r',encoding='utf-8')
except (IndexError,KeyError) as e:  #没有IndexError,KeyError这两个异常
    print(e)
except Exception as e:  #只能通过这个异常处理，Exception 抓住所有的异常
    print(e)"""
# else作用,#没有异常出错，走else的逻辑代码

"""try:
    print('qiqiao') #代码没有异常
except (IndexError,KeyError) as e:
    print(e)
except Exception as e:
    print(e)
else:           #没有异常出错，走else的逻辑代码
    print('没有异常')"""
# finnally作用,不管有没有错，都这行finnally
#没有异常出错，走else的逻辑代码
"""try:
    print('qigao,handson')  # 没有异常
except (IndexError, KeyError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("不管有没有错，都这行finnally")"""
#有异常出错
"""name = [1, 2, 3]
data = {'a':'b'}
try:
    data["c"] # data字典中没有'c'这个key值
    name[6]
except (IndexError, KeyError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("不管有没有错，都这行finnally")"""
#自定义异常:自定义使用总结：
# 数据库连接不上的信息
# 权限问题，解析是没有权限了，给出异常提示
# 业务逻辑的错误
"""class GaoError(Exception):  # 定义一个异常类，继承Exception

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message  # 给对象取一个名

try:
    raise GaoError("数据库连接不上了")  # 触发自定义异常，GaoError("数据库连接不上了")这个对象
except GaoError as e:
    print(e)"""
# assert 断言
"""def a(a,b):
    s = [a,b]
    print(len(s))
    s.reverse()
    s.append('1.2')
    assert(len(s)>=5)  #不希望s的长度大于2   大于等于3则包vu哦,只有三个参数
    return s
print(a(3,4))"""
class C(object):
    def __init__(self):
        self.name = 'AAA'
c1 = C()
assert c1.name == 'AAA'  #断言
print("没有错误,继续...")
assert c1.name == 'BBB'  #断言不符合,报错
print("断言报错")
# if else捕获异常
"""class B(object):
    def __init__(self):
        self.name = 'nn'
c2 = B()
if c2.name == 'nn':
    print("有错误")
else:
    print("没错")"""


class C(object):

    def __init__(self):
        self.name = "zhangqigao"


c_obj = C()

if c_obj.name != "gaogao":
    print("不等于,有错误....")
else:
    print("没有错误继续...")