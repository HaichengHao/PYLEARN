# editor: 百年
# time: 2024/2/15 11:51
import requests
import random
proxies_pool=[
    {'http':'139.196.111.167:9000'},
    {'http':'222.138.76.6:9002'},
    {'http':'123.182.58.59:8089'},
    {'http':'36.6.144.126:8089'},
    {'http':'117.160.250.134:8899'},
    {'http':'1.15.47.213:443'},
    {'http':'58.253.210.122:8888'},
    {'http':'39.105.5.126:80'},
    {'http':'117.74.65.207:80'},
    {'http':'36.6.144.232:8089'},
    {'http':'36.6.145.196:8089'},
    {'http':'111.225.152.134:8089'},
]
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',

}
proxies=random.choice(proxies_pool)
url='https://www.baidu.com'
response=requests.get(url=url,headers=headers,proxies=proxies)

# 一个类型和6个属性
print(type(response))
# <class 'requests.models.Response'> <--注意，这里与urllib不一样
# urllib的类型是 <class 'http.client.HTTPResponse'> 类型为 HTTPResponse 即超文本传输协议响应类型

# .encoding 设置响应的编码格式
response.encoding='utf-8'


# .text() 以字符串的形式返回了网页源码
print(response.text)

# .url() 返回链接地址
print(response.url)
# https://www.baidu.com/

# .content 返回二进制的数据，用的不多
print('----------')
print(response.content)

# .status_code 返回响应的状态码
print(response.status_code)

# .headers 返回响应头信息
print(response.headers)

