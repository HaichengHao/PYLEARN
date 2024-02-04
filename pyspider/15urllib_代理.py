# editor: 百年
# time: 2024/2/4 19:44
import urllib.request
import random
proxies_pool=[
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
    # {'http':'183.164.242.65:8089'},
    {'http': '120.25.222.150:1080'},
    {'http': '101.39.205.10: 1080'},
    {'http': '117.160.250.131: 8899'},
    {'http': '60.247.225.197:8880'},
    {'http': '47.100.184.89:80'},
    {'http': '139.196.78.175:7890'},
    {'http': '117.50.108.90:7890'},
    {'http': '49.232.48.123:9999'},
    {'http': '58.87.103.164:8118'},
    {'http': '61.52.175.152:9999'},
'''	

49.7.11.187	80	HTTP	普匿	北京市 电信
120.197.40.219	9002	HTTP	普匿	广东省广州市 移动
222.243.201.153	9992	HTTP	普匿	湖南省永州市 电信
117.69.236.98	8089	HTTP	未知	安徽省淮北市 电信
113.223.213.88	8089	HTTP	高匿	湖南省衡阳市 电信
220.248.70.237	9002	HTTP	普匿	上海市 联通
117.160.250.131	8899	HTTP	普匿	河南省 移动/数据上网公共出口
47.106.144.184	7890	HTTP	高匿	广东省深圳市 阿里云
183.215.23.242	9091	HTTP	普匿	湖南省长沙市 移动
183.164.242.98	8089	HTTP	高匿	安徽省淮北市 电信
39.98.204.54	7890	HTTP	高匿	北京市 阿里云'''
    # {'http':'183.221.242.103:9443'},
    # {'http':'183.230.198.80:9091'},
    # {'http':'183.221.242.103:9443'},
    # {'http':'183.230.198.80:9091'},
    # {'http':'58.220.95.79:10000'},
    # {'http':'121.8.215.106:9797'},
    # {'http':'221.226.75.86:55443'},
    # {'http':'183.247.152.98:53281'},
    # {'http':'61.133.66.69:9002'},
    # {'http':'118.31.1.145:80'},
    # {'http':'114.55.176.250:80'},
    # {'http':'120.26.217.192:80'},
    # {'http':'120.55.243.66:80'},
    # {'http':'218.57.210.186:9002'}
]
proxies=random.choice(proxies_pool)
print(proxies)
url='https://ip.tool.chinaz.com/'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
# 获取响应信息
content=response.read().decode('utf-8')
with open('./demo15.html','w+',encoding='utf-8') as wfp:
    wfp.write(content)