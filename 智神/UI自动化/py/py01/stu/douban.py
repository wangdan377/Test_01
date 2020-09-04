import requests
# r = requests.get('https://api.github.com/events')
r = requests.get('http://www.baidu.com/')

print(r.json())