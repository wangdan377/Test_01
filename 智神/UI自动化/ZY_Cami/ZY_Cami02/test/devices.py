from appium import webdriver
class devic(object):
    '''美颜'''
    """def __init__(self):
        # self.driver = self.devices()    #感觉是这里的问题
        # self.driver = 'driver'
        pass"""
    def devices01(self):

        """desired_caps = {}
        desired_caps['platformName'] = 'Android'  # Android系统 or IOS系统
        desired_caps['deviceName'] = '7HX0219918017044'  # 真机或模块器名
        desired_caps['platformVersion'] = '10'  # Android系统版本
        desired_caps['appPackage'] = 'com.zhiyun.cama'  # APP包名
        desired_caps['appActivity'] = '.splash.SplashActivity'  # APP启动Activity
        desired_caps['noReset'] = True  # 每次打开APP不开启重置，否则每次都进入四个欢迎页
        desired_caps['resetKeyboard'] = True  # 隐藏键盘        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动APP
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)"""  # 启动APP
        desired_caps = {'platformName': 'Android',  # 手机系统
                        'deviceName': '7HX0219918017044',
                        'noReset': True,  # 防止每次启动时软件初始化
                        'appPackage': 'com.zhiyun.cama',
                        'appActivity': '.splash.SplashActivity',
                        'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串
                        'resetKeyboard': True}  # 将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        desired_caps['newCommandTimeout'] = 6000
        self.driver.implicitly_wait(15)
        # print('启动app')
        return self.driver

b = devic()
b.devices01()