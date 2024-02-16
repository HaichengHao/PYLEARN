# editor: 百年
# time: 2024/2/15 12:07
'''
梳理urllib知识点来映射requests
'''
import random

import requests
proxies_pool=[
    {'http': '114.231.45.39	:8888'},
    {'http': '183.64.239.19	:8060'},
    {'http': '218.75.69.50	:57903'}
    # {'http':'114.231.45.14	:8888'},
    # {'https':'125.87.88.234:19961'},
    # {'http':'183.236.232.160:8080'},
    # {'http':'218.75.69.50:57903'},
    # {'http':' 114.231.45.14	:8888'},
    # {'http':' 114.231.41.71:8888'},
    # {'http':' 47.97.191.179:8018'},
    # {'http':' 183.64.239.19:8060'},
    # {'http':' 218.75.102.198:8000'},
    # {'http':' 182.140.244.163:8118'},
    # {'http':'139.196.111.167:9000'},
    # {'http':'222.138.76.6:9002'},
    # {'http':'123.182.58.59:8089'},
    # {'http':'36.6.144.126:8089'},
    # {'http':'117.160.250.134:8899'},
    # {'http':'1.15.47.213:443'},
    # {'http':'58.253.210.122:8888'},
    # {'http':'39.105.5.126:80'},
    # {'http':'117.74.65.207:80'},
    # {'http':'36.6.144.232:8089'},
    # {'http':'36.6.145.196:8089'},
    # {'http':'111.225.152.134:8089'},
]
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
}
proxies=random.choice(proxies_pool)
print(proxies)
url='http://www.baidu.com/s'
data={
    'wd':'牛撒撇'
}
# params 参数
# 注意，requests直属于python，相对于urllib,它不需要对data进行encode操作

response=requests.get(url=url,headers=headers,data=data)
response.encoding='utf-8'
content=response.text
print(content)

