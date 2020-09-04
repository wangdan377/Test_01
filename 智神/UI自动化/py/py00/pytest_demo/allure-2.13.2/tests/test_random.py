import random


# 写一个随机取数函数
def get_random_int():
    return random.randint(1,6)


# 假装测试上面的函数
def test_random():
    r = get_random_int()
    print(r)
    assert r in range(1,5)