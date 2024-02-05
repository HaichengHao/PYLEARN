# editor: 百年
# time: 2024/2/5 13:54
import urllib.request
from lxml import etree
import random
# proxies_pool=[
#     {'http':'139.196.111.167:9000'},
#     {'http':'222.138.76.6:9002'},
#     {'http':'123.182.58.59:8089'},
#     {'http':'36.6.144.126:8089'},
#     {'http':'117.160.250.134:8899'},
#     {'http':'1.15.47.213:443'},
#     {'http':'58.253.210.122:8888'},
#     {'http':'39.105.5.126:80'},
#     {'http':'117.74.65.207:80'},
#     {'http':'36.6.144.232:8089'},
#     {'http':'36.6.145.196:8089'},
#     {'http':'111.225.152.134:8089'},
#     {'http':'183.164.242.65:8089'},
#     {'http': '120.25.222.150:1080'},
#     {'http': '101.39.205.10: 1080'},
#     {'http': '117.160.250.131: 8899'},
#     {'http': '60.247.225.197:8880'},
#     {'http': '47.100.184.89:80'},
#     {'http': '139.196.78.175:7890'},
#     {'http': '117.50.108.90:7890'},
#     {'http': '49.232.48.123:9999'},
#     {'http': '58.87.103.164:8118'},
#     {'http': '61.52.175.152:9999'}]

# proxies=random.choice(proxies_pool)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Cookie':'BDUSS=0hETn5PM0liUFhWbVlyaElZUjVFeTlMZmdqUGFQY3oxQVRRcTJDMTZ1QUlmWk5sRVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjwa2UI8GtlZ; BDUSS_BFESS=0hETn5PM0liUFhWbVlyaElZUjVFeTlMZmdqUGFQY3oxQVRRcTJDMTZ1QUlmWk5sRVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjwa2UI8GtlZ; PSTM=1706843334; BD_UPN=12314753; BIDUPSID=F2BDCD40C8DDDC65B56CC32AD1D160A6; H_PS_PSSID=40202_40079_40206_40211_40222; BA_HECTOR=0k8k808k012g0h212gak8l21h6et7r1irv0sj1s; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; B64_BOT=1; ZFY=LEpoPkGxuKaEf44QLs4U02bPnj9UA:AeWnHDfElJQ00o:C; baikeVisitId=293b33af-3712-4b1b-82cb-ec44c5d8c08e; COOKIE_SESSION=82109_0_3_4_0_1_1_0_3_1_1_0_0_0_0_0_0_0_1678114280%7C4%230_0_1707054423%7C1%7C1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=1; H_PS_645EC=575fSHpA105VWlVgVFkiRZRJaDkJRIiLdBtw9iomIJPSIqWETYw8%2FxwOwGg; BAIDUID=E2F8DB8F78AF62593D904035D2A2BC54:SL=0:NR=10:FG=1; BAIDUID_BFESS=E2F8DB8F78AF62593D904035D2A2BC54:SL=0:NR=10:FG=1; sug=3; sugstore=1; ORIGIN=0; bdime=0'
}
url='https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E7%83%AD%E6%90%9C'
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)

# request=urllib.request.Request(url=url,headers=headers)
# handler=urllib.request.ProxyHandler(proxies=proxies)
# opener=urllib.request.build_opener(handler)
# response=opener.open(request)
content=response.read().decode('utf-8')
print(content)
# 解析服务器响应的文件
tree=etree.HTML(content)
answer=tree.xpath('//span[@class="bg s_btn_wr"]/input/@value')[0]
print(answer)


