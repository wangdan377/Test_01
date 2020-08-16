import requests
#
# def request(url, headers, param, typed='get'):
#     if typed == 'get':
#         response = requests.get(url=url, headers=headers)
#         if response.status_code == 200:
#             return response
#         elif response.status_code == 409:
#             return response
#         else:
#             raise ValueError("调用接口失败，状态码为：%s,返回信息为：%s" %((response.status_code),response.json))
#
#     elif typed == 'post':
#         response= requests.post(url=url,headers=headers, json=param)
#         if response.status_code == 200:
#             return response
#         else:
#             raise ValueError("调用接口失败，状态码为：%s,返回信息为：%s" %((response.status_code),response.json))

def request(url1,headers1, param1, typed="get"):
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
