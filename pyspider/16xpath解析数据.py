# editor: 百年
# time: 2024/2/5 9:50
# xpath可以解析两种文件
# 1.解析本地文件 etree.parse('xxx.html')
# 2.解析服务器响应 etree.HTML(content)

'''
模糊查询
eg://div[contains(@id,“tb")]/text() 查询含有属性为tb俩字母的div
eg://div[starts-with(@id,"tb")]/text() 查询id的值，查询以"tb"开头的div

逻辑运算
eg:查询id为l1和class为c1的li
//li[@id="l1" and @class="c1"]/text()

eg:
//li[@id="l1"]/text() | //li[@id="l2"]/text()
'''
import random
import urllib.request
from lxml import etree

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
    {'http':'183.164.242.65:8089'},
    {'http': '120.25.222.150:1080'},
    {'http': '101.39.205.10: 1080'},
    {'http': '117.160.250.131: 8899'},
    {'http': '60.247.225.197:8880'},
    {'http': '47.100.184.89:80'},
    {'http': '139.196.78.175:7890'},
    {'http': '117.50.108.90:7890'},
    {'http': '49.232.48.123:9999'},
    {'http': '58.87.103.164:8118'},
    {'http': '61.52.175.152:9999'}]
proxies=random.choice(proxies_pool)

url='https://www.taobao.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/'
    }
request=urllib.request.Request(url=url,headers=headers)
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
print(content)

tree=etree.HTML(content)
goods_info=tree.xpath('//div[@class="tb-recommend-content clearfix"]/div[@class="tb-recommend-content-item"][1]/a/div[@class="info-wrapper"]/div[@class="title"]/text()')
print(goods_info.extract())  #


