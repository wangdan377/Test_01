import requests

def request(url, headers, param, typed='get'):
    if type == 'get':
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
            raise ValueError("调用接口失败，状态码为：%s,返回信息为：%s" %((response.status_code),response.json))
