# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 15:53
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import xlwt
import json
from  common.http_requests import http_requests


class  get_swagger():
    # 发送请求，获取swagger中的json数据
    def __init__(self,url):
        self.res = http_requests().http_requests(url, "get").json()

    def swagger_data(self):
        get_swagger_data = []
        data_paths = self.res["paths"]
        for http_url_data in data_paths.keys():
            swagger_data = {}
            swagger_data["http_url"] = http_url_data
            http_mthods = list(data_paths[http_url_data].keys())  # 提取data[i]中的key值
            for http_mthod in http_mthods:
                swagger_data["http_mthod"] = http_mthod  # 获取url对应的http_mthod
                value = data_paths[http_url_data][http_mthod]
                key0 = ("tags", "summary", "operationId", "consumes", "parameters", "responses")
                for key in key0:
                    if key not in value.keys():
                        value[key] = 'None'
                    else:
                        pass
                swagger_data["summary"] = str((value["summary"]))  # 获取url对应的summary
                swagger_data["operationId"] = str(value["operationId"])  # 获取url对应的operationId
                swagger_data["consumes"] = str(value["consumes"])  # 获取url对应的consumes
                swagger_data["responses"] = json.dumps(value["responses"])  # 获取url对应的responses
                swagger_data["parameters"] = json.dumps(value["parameters"])  # 获取url对应的parameters
                swagger_data["tags"] = str(value["tags"][0])
                # 设置swagger_data对应的tags说明
                for tags_data in self.res["tags"]:#遍历tags的数据
                    if  swagger_data["tags"] == tags_data["name"]:
                        swagger_data["tags_des"] = tags_data["description"]#获取tags对应的说明信息
                    else:
                        pass
                # 获取parameters中name的值
                if swagger_data["parameters"] != '"None"':#判断parameters不为空的数据
                    parameters = json.loads(swagger_data["parameters"])
                    http_parame = {}
                    for parame_data in parameters:  # 遍历parameters中的name
                        name = str.upper(parame_data["name"])#将parameters中的name求值转换为大写
                        defi = {}
                        for a, b in self.res["definitions"].items():
                            defi[(a.upper())] = b#将definitions中key值全部转换为大写
                        if name in defi:#若definitions中key与parameters中的name匹配，将替换parameters的信息
                            http_parame = defi[name]["properties"]
                        else:
                            http_parame[parame_data["name"]] = ""#不匹配，直接将parameters中的name设置为http_parame的key
                    swagger_data["parame_data"] = json.dumps(http_parame)
                else:
                    swagger_data["parame_data"] = 'None'
                print(swagger_data)
            get_swagger_data.append(swagger_data)
        return get_swagger_data#返回获取的data,并存到一个列表中

    def excel_data(self,sheet):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet(sheet)
        #设置表头
        data_excle = self.swagger_data()#获取self.swagger_tata()
        table = list(data_excle[0].keys())  #获取健值，将其转化为list
        for i in range(0, len(table)):
            worksheet.write(0, i, table[i])
        #写入数据
        for j in range(0, len(data_excle)):
            m = 0
            ls = list(data_excle[j].values())
            for k in ls:
                worksheet.write(j + 1, m, k)
                m += 1
        workbook.save('excel_tata.xls') #保存excel

if __name__ == '__main__':
    url = "/auth-internet/v2/api-docs?group=authority"
    test = get_swagger(url).swagger_data()

    # test2 = get_swagger(url).excel_data("auth-internet")


