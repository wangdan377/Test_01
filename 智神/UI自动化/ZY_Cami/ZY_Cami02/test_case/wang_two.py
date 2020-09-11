"""from test_case.wang_one import oneDay
class twoDay(object):
    def __init__(self):
        self.age = 12
    def gorun(self):
        oneday = oneDay()
        oneday.run()

if __name__ == '__main__':
    shili = twoDay()
    shili.gorun()
"""

from test_case.wang_one import oneDay
class twoDay(object):
    def __init__(self):
        self.age = 12
        self.oneday = oneDay()
    def gorun(self):
        # oneday = oneDay()
        self.oneday.run()           #只打印函数内的print
        print(self.oneday.run())    #所有的都打印
if __name__ == '__main__':
    shili = twoDay()
    shili.gorun()