
"""#叠加的数据类型里的值也可以叠加地取出来
my_dict = {
    "零食" : ["蛋糕","巧克力","牛奶","薯片"],
    "零钱" : 45,    #int对象不能取下标
    "天气" :"晴"
}
print(my_dict["零食"][0])
print(my_dict["天气"][0])"""
inventory = {
    "零钱": 500,
    "小口袋":['小刀','绳子','手套'],
    "大口罩":['帐篷', '水杯', '睡袋', '毛巾']
}

inventory['电子设备'] = ['平板,' '手机', '相机']  #添加一个列表
inventory['电子设备'].append('电脑')    #对应的list添加一个元素
inventory['化妆品'] = "洗面奶"    #添加一个元素
inventory['小口袋'].sort()    #进行排序
# inventory["零钱"].append()

print(inventory)


