from test_case.wang_one import oneDay
class twoDay(object):
    def __init__(self):
        self.age = 12
    def gorun(self):
        oneday = oneDay()
        oneday.run()

if __name__ == '__main__':
    shili = twoDay()
    shili.gorun()
