# editor: 百年
# time: 2024/2/25 21:01
import requests
from lxml import etree
import random
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
}
proxies_pool=[
    {'http':'36.6.144.211:8089'},
    {'http':'122.224.56.198:7302'},
    {'http':'114.231.46.219:8089'},
    {'http':'114.231.8.62:8089'},
    {'http':'117.71.133.250:8089'},
    {'http':'183.164.243.43:8089'},
    {'http':'117.71.132.193:8089'},
    {'http':'117.57.92.79:8089'},
    {'http':'114.231.45.121:8888'},
    {'http':'183.164.243.152:8089'},
    {'http':'117.71.154.151:8089'},
    # {'http':'183.164.242.102:8089'},
    {'http':'117.69.232.167:8089'},
    {'http':'103.237.78.102:4995'},
    # {'http':'183.164.242.31:8089'},
    {'http':'36.6.144.229:8089'},
    {'http':'117.71.149.251:8089'},
    {'http':'183.164.243.223:8089'},
    {'http':'117.71.155.92:8089'},
    {'http':'117.71.154.250:8089'},
    {'http':'117.71.154.237:8089'},
    {'http':'121.40.119.213:80'},
    {'http':'121.40.94.50:80'},
    {'http':'114.55.179.125:80'},
    {'http':'121.43.103.197:80'},
    # {'http':'120.55.241.19:80'},
    {'http':'120.26.15.184:80'},
    {'http':'116.62.32.225:80'},
    {'http':'116.62.35.202:80'},
    {'http':'120.26.12.52:80'},
    {'http':'116.62.238.186:80'},
    {'http':'49.71.141.163:7788'},
    {'http':'112.124.33.87:80'}, #<--可以用的
    {'http':'221.194.147.196:80'},
    {'http':'101.37.80.123:80'},
    {'http':'118.31.105.240:80'},
    {'http':'120.55.242.178:80'},
    {'http':'121.41.54.26:80'},
    {'http':'101.37.24.91:80'},
    {'http':'221.230.216.74:7788'},
]
proxies=random.choice(proxies_pool)
print('当前使用的代理是{0}'.format(proxies))
url='https://www.btwuji.com/html/gndy/china/index.html'
response=requests.get(url=url, headers=headers,proxies=proxies)
response.encoding='gb2312'
source=response.text
print(source)
with open('./dytt.html','a+',encoding='utf-8') as wfp:
    wfp.write(source)