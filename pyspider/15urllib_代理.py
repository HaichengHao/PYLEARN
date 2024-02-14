# editor: 百年
# time: 2024/2/4 19:44
import urllib.request
import random
proxies_pool=[
    {'http':'117.69.236.15:8089'},
    # {'https': '60.205.216.70:7777'},
    # {'https':'117.57.93.59:8089'}
]
proxies=random.choice(proxies_pool)
print(proxies)
# url='https://ip.tool.chinaz.com/'
# url='https://www.ip138.com/'
url='https://www.ipaddress.my/?lang=zh_cn'
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