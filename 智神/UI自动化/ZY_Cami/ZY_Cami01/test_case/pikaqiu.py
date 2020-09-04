import os,re
from selenium import webdriver
import datetime
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datelist.dianji_enter import get_enter
from selenium.webdriver.common.keys import Keys


def ones(driver,dates):
    #首页操作
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="create-digital-button"]/span/input').click()
    except:
        pass
    time.sleep(5)
    driver.find_element_by_id('data-title').send_keys(dates[1])
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="series-title-field"]/div[1]/span/span/input').send_keys(dates[0])
    driver.find_element_by_xpath('//*[@id="series-number-field"]/div[1]/span/span/input').send_keys(str(dates[2]))
    time.sleep(3)
    driver.find_element_by_id('data-primary-author-first-name').send_keys('123')
    driver.find_element_by_id('data-primary-author-last-name').send_keys('456')
    time.sleep(3)
    time.sleep(1)
    driver.find_element_by_id('data-desc').send_keys('''{}'''.format(dates[3]))
    time.sleep(3)
    driver.find_element_by_id('non-public-domain').click()
    time.sleep(1)
    tags = dates[4]
    one_tag(driver,tags)
    driver.find_element_by_id('data-button-proto-announce').click()
    catagory = []
    cates = dates[5]
    for i in cates:
        if not i in catagory:
            catagory.append(i)
    one_cate(driver,catagory)

def one_tag(driver,tags):
    #首页标签选择
    try:
        driver.find_element_by_id('data-keywords-0').send_keys('{}'.format(tags[0]))
        driver.find_element_by_id('data-keywords-1').send_keys('{}'.format(tags[1]))
        driver.find_element_by_id('data-keywords-2').send_keys('{}'.format(tags[2]))
        driver.find_element_by_id('data-keywords-3').send_keys('{}'.format(tags[3]))
        driver.find_element_by_id('data-keywords-4').send_keys('{}'.format(tags[4]))
        driver.find_element_by_id('data-keywords-5').send_keys('{}'.format(tags[5]))
        driver.find_element_by_id('data-keywords-6').send_keys('{}'.format(tags[6]))
    except:
        pass
    time.sleep(6)

def one_cate(driver,category):
    #首页关键字输入
    print(category)
    time.sleep(3)
    ibox = 'checkbox-'
    for i in category:
        flags = category.index(i) - 1
        if i == category[3]:
            ibox = re.sub(category[flags].lower(), i.lower(), ibox)

        else:
            ibox += i.lower() + '_'
        print(i)
        try:
            xpath_gz = "//*[text()='{}']/parent::*".format(i)
            print(xpath_gz)
            driver.find_element_by_xpath(xpath_gz).click()
        except:
            try:
                xpath_gz = "//a[text()='{}']/parent::*".format(i)
                print(xpath_gz)
                driver.find_element_by_xpath(xpath_gz).click()
            except:
                try:
                    xpath_gz = "//label[text()='{}']/parent::*".format(i)
                    print(xpath_gz)
                    driver.find_element_by_xpath(xpath_gz).click()
                except:
                    try:
                        xpath_gz = "//span[text()='{}']/parent::*".format(i)

                        print(xpath_gz)
                        try:
                            driver.find_element_by_xpath(xpath_gz).click()
                        except:
                            driver.find_element_by_xpath(xpath_gz).click()
                    except:
                        try:
                            xpath_gz = "//*[text()='{}']/preceding-sibling::input".format(i)
                            print(xpath_gz)
                            driver.find_element_by_xpath(xpath_gz).click()
                        except:
                            print(ibox)
                            driver.find_element_by_id(ibox[:-1]).click()


        time.sleep(5)
    driver.find_element_by_xpath('//*[@id="category-chooser-ok-button"]/span/input').click()
    time.sleep(3)
    driver.find_element_by_id('save-and-continue-announce').click()

def twos(driver,dates):
    #第二个页面文件上传
    print('121212')
    time.sleep(10)
    print('123')
    driver.find_element_by_xpath('//*[@id="data-is-drm"]/div/div/div[1]/div/label/input').click()
    time.sleep(3)

    driver.find_element_by_id('data-file-upload-AjaxInput').send_keys(r'{}'.format(dates[7]))
    time.sleep(35)
    driver.find_element_by_xpath('//*[@id="data-choice-accordion"]/div[2]/div/div[1]/a/i').click()
    time.sleep(3)
    driver.find_element_by_id('data-cover-file-upload-AjaxInput').send_keys(r'{}'.format(dates[6]))
    time.sleep(50)
    driver.find_element_by_id('save-and-continue-announce').click()
    time.sleep(180)
def threes(driver,prices):
    #操作第三个界面
    time.sleep(20)
    driver.find_element_by_id('data-is-select').click()
    time.sleep(3)
    if prices < 2.99:
        driver.find_element_by_xpath('//*[@id="data-rate"]/div/div/div[1]/div/label/input').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="data-input"]/input').send_keys(str(prices))
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="data-is-lending"]').click()
        time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="data-rate"]/div/div/div[2]/div/label/input').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="us-price-input"]/input').send_keys(str(prices))
        time.sleep(3)

    driver.find_element_by_xpath('//*[@id="save-publish-announce"]').click()

    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="a-2"]/div/header/button').click()
    # get_enter()
    print('运行完成！')

def amazon_main(dates):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    chrome_driver = r"C:\Users\py\Desktop\gongzuo\post_amazon\chromedriver.exe"
    #谷歌浏览器启动插件
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    print(dates)
    ones(driver,dates)
    twos(driver,dates)
    threes(driver, 0.99)