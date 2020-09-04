import requests

"""def request(url, headers, param, typed='get'):
    if typed == 'get':
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response
        elif response.status_code == 409:
            return response
        else:
            raise ValueError("调用接口失败，状态码为：%s,返回信息为：%s" %((response.status_code),response.json))

    elif typed == 'post':
        response= requests.post(url=url,headers=headers, json=param)
        if response.status_code == 200:
            return response
        else:
            raise ValueError("调用接口失败，状态码为：%s,返回信息为：%s" %((response.status_code),response.json))"""

"""def request(url1,headers1, param1, typed="get"):
    if typed == "get":
        response = requests.get(url=url1,headers=headers1, params=param1)
        if  response.status_code == 200:
            return response
        elif response.status_code == 409:
            return response
        else:
            raise ValueError("调用接口失败,状态码为: %s ,返回信息为：%s" % ((response.status_code),response.json()))
    elif typed == "post":
        response= requests.post(url=url1,headers=headers1, data=param1)
        if response.status_code == 200:
            return response
        elif response.status_code == 409:
            return response
        else:
            raise ValueError("调用接口失败,状态码为: %s ,返回信息为：%s" % ((response.status_code), response.json()))
"""
"""class requestMethod:
    def get_post(self,url,header,params,files=None):
        if files is not None:
            res=requests.post(url=url,headers=header,data=params,files=files,timeout=15)
        else:
            res=requests.post(url=url,headers=header,data=params,timeout=15)
        return res

    def get_get(self,url,header,params=None):
        if params is not None:
            res=requests.get(url=url,headers=header,params=params)
        else:
            res=requests.get(url=url,headers=header)
        return res"""


"""def request(url1,headers1,param1=None, typed="get"):
    if typed == "get":
        if param1 is not None:
            response = requests.get(url=url1,headers=headers1, params=param1)
            return response
        else:
            reresponses=requests.get(url1,headers1)
            return reresponses

    elif typed == "post":
        response= requests.post(url=url1,headers=headers1, json=param1)
        return response"""


def get_post(url,header,params=None):
    if params is not None:
        res=requests.post(url=url,headers=header,data=params)
    else:
        res=requests.post(url=url,headers=header)
    return res

def get_get(url,header,params=None):
    if params is not None:
        res=requests.get(url=url,headers=header,params=params)
    else:
        res=requests.get(url=url,headers=header)
    return res