
import HTMLTestRunnerCN3_pie_chart_screen

import HTMLTestRunnerCN
from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner,logging
from common.loged import Logger
from selenium.common.exceptions import  NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

log = Logger('D:\ZY_Cami03\logs\\all.log',level='debug')




class Beautify_Fair(unittest.TestCase):
    '''美颜'''
    @classmethod
    def setUp(self):
        print('start test','启动app')
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

    @classmethod
    def tearDown(self):
        print('end test')

    def test_connecting00(self):  # 不连接相机/不连接设备
        driver = self.driver
        try:
            driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()
            time.sleep(5)
            driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()  # 点击帮助
            driver.get_screenshot_as_file('../screen/test_connecting00.png')
            driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
            # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
            time.sleep(5)
        except NoSuchElementException as a: #元素不存在，则调用捕获异常处理
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(a)
            driver.get_screenshot_as_file('../screen/test_connecting00.png')
        try:
            driver.find_element_by_id("com.zhiyun.cama:id/iv_beauty").click()  # 美颜
            time.sleep(2)
        # driver.find_element_by_id("com.zhiyun.cama:id/sb_roll").click()     #进度条	[533,150][732,1066]     199  916
        # driver.tap([(1180,540)])  #点击空白区域
        # driver.tap([(632, 1022)])   #横坐标632  #纵坐标1022
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(a)
        """except NoAlertPresentException as b:   #捕获意外的异常
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(b)
            driver.get_screenshot_as_file('../screen/test_login.png')
        except Exception as result:     #捕获异常
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(result)
            driver.get_screenshot_as_file('../screen/test_login.png')
        else:
            pass  #没有错的情况下执行
        finally:
            pass  #有没有错，都会执行
        return ''"""
    """def connecting01(self):   #不连接相机/不连接设备
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()  # 相机
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()   #点击帮助
        driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
        # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
        time.sleep(5)
        return '不连接相机/不连接设备'
        
        '''if self.connecting01()  is  on :
            print('继续运行')
        else:
            try:
                driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()
            except Exception as e:
                log.logger.critical(e)'''


        '''try:
            driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()
        except Exception as e:
            log.logger.critical(e)'''
        '''while True:
            try:
                pic.connecting01()
            except Exception as e:
                log.logger.critical(e)'''
        #元素是否存在
        '''try:
            cameras = driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()
        except NosuchElementException: #元素不存在，则调用捕获异常处理
            print('没有这个元素')
        else:
            cameras.click()'''"""


    """def test_beautify_01(self):     #美颜
        driver = self.driver
        try:
            driver.find_element_by_id("com.zhiyun.cama:id/iv_beauty").click()     #美颜
            time.sleep(2)
        # driver.find_element_by_id("com.zhiyun.cama:id/sb_roll").click()     #进度条	[533,150][732,1066]     199  916
        # driver.tap([(1180,540)])  #点击空白区域
        # driver.tap([(632, 1022)])   #横坐标632  #纵坐标1022
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(a)
            # driver.get_screenshot_as_file('../screen/test_connecting00.png')
        '''except NoAlertPresentException as b:  # 捕获意外的异常
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(b)
            driver.get_screenshot_as_file('../screen/test_login.png')
        except Exception as result:  # 捕获异常
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(result)
            driver.get_screenshot_as_file('../screen/test_login.png')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行'''
        return ''"""
    """def slides01(self): #向上滑动
        driver = self.driver
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        driver.swipe(x * 0.15, y * 0.8, x * 0.15, y * 0.3, 200)  # 向上滑动
        time.sleep(2)
        return '向上滑动'
    def slides02(self):
        driver = self.driver
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        driver.swipe(x * 0.15, y * 0.3, x * 0.15, y * 0.8, 200)  # 向下滑动
        time.sleep(2)
        return '向下滑动'
    def beautify_02(self):     #自动美颜
        driver = self.driver
        self.slides01()   # 调用slides函数（向上滑动）
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]").click()  # 自动美颜 无进度条
        return '向上滑动，自动美颜'
    def blank_01(self):     #点击空白区域
        driver = self.driver
        driver.tap([(1180, 540)])  # 点击空白区域
        return '点击空白区域，关闭美颜'
    def beautify_03(self):     #取消美颜
        driver = self.driver
        self.beautify_01() #美颜
        self.slides01()  #向上滑动
        time.sleep(2)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()  # 取消美颜
        return '向上滑动，取消美颜'

    def beautify_04(self):      #瘦脸
        driver = self.driver
        self.beautify_01()     #点击美颜
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]").click()        #瘦脸
        return '瘦脸'
    def beautify_05(self):     #磨皮
        self.beautify_01()    #点击美颜
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()		 #磨皮
        return '磨皮'


    def beautify_06(self):  # 美白
        driver = self.driver
        self.slide()   #滑动进度条
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]").click()		  #美白
        self.slide()  # 滑动进度条

        return '美白'
    def slide(self):        #滑动
        driver = self.driver
        driver.tap([(632, 1022)])
        return '滑动'
    def beautify_07(self):  # 眼睛放大
        driver = self.driver
        self.slides02()  # 向下滑动
        time.sleep(2)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]").click()		   #眼睛放大
        return '眼睛放大'

    def beautify_08(self):  # 光照
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()		 #光照
        return '光照'

    def beautify_09(self):  # 红润
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]").click()		#红润
        return '红润'

    def picture_01(self):  # 点击拍照
        driver = self.driver
        self.blank_01()   #点击空白区域
        driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()		#拍照
        # 循环
        '''num = 0
        for i in range(5):   
            try:
                num = num + 1
                driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()
            except:
                try:
                    num = num -1
                    driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()
                except:
                    num = num - 2
                    driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()'''
        return '点击拍照 '"""

def Suit():
    suite = unittest.TestSuite()
    # AddTest是要测试的类名，test_01是要执行的测试方法
    suite.addTest(Beautify_Fair("test_connecting00"))
    # suite.addTest(Beautify_Fair("test_beautify_01"))
    return suite

if __name__ == '__main__':
    unittest.main()

    # pic = Beautify_Fair()
    # print(pic.test_devices())
    # print(pic.test_connecting00())
    # print(pic.connecting01())
    # print(pic.beautify_01())
    # print(pic.slides01())
    # print(pic.slides02())
    # print(pic.beautify_02())
    # print(pic.blank_01())
    # print(pic.beautify_03())
    # print(pic.beautify_04())
    # print(pic.beautify_05())
    # print(pic.beautify_06())
    # print(pic.slide())    #滑动
    # print(pic.beautify_07())
    # print(pic.beautify_08())
    # print(pic.beautify_09())
    # print(pic.picture_01())
    """soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = '../report/' + now + 'result.html'  # 第一种方法,相对路径下
    '''# filename = '../report/report' + now + 'result.html'  # 第二种方法,相对路径下+report报告名字
    # filename = '../report'+ os.sep+ 'report' + now + 'result.html'    #第二种方法,相对路径下,上级目录../report文件夹下,分隔符下文件名  os.sep+ 'report'
    # filename = os.getcwd() + os.sep+ 'report' + now + 'result.html'   #相对路径下,该路径下的,所以就到test_case下面了
    # filename = os.path.dirname(os.path.dirname(__file__))+ os.sep + 'report' + now + 'result.html'  #相对路径下,该路径下的,所以就到test_case下面了
    # filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'   #绝对路径下
    # filename = '../' + now + 'result.html'   #../是上级目录,还是在上级目录下
    # filename = '../' + os.sep + 'report' + now + 'result.html'   #还是在上级目录下
    # filename = '../report' + now + 'result.html'  #还是在上级目录下'''
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',
                                                               device=(soundbox_device),
                                                               description='用例执行情况:')
    # runner.run(suite)
    runner.run(Suit())
    fp.close()"""