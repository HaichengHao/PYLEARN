# editor: 百年
# time: 2024/2/16 17:32
import random

import requests
headers={
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Cookie':'BAIDUID_BFESS=CA59DFBCAA61D8EFEB819A18BBC5F507:FG=1; BIDUPSID=CA59DFBCAA61D8EFEB819A18BBC5F507; PSTM=1707878929; H_PS_PSSID=39996_40169_40204_39662_40207_40211_40216_40223; ZFY=IGGFluIQbd5UgDz9bs7Z:AWOGW6bQRThHXMa2zZZOBu0:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1706949510,1708076440; APPGUIDE_10_6_9=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_OTgwMjk1NGQ3ODg2Y2FlZTVjZTE4OTY1Mjk3OGFkOGMxMjI4NDQzYmZiZDk2ODNmOWEwYWEwMTQ0Njc4OTJlYzI1ZGIwNjk2MDYyOWMxOWRkZGViOWFlNzU2ZTc0NTJmOGI0MTk0MDc5NWUwYzFiNTQyOGZhZjZmMGNiOGRmMjhhMzg3NzE5M2EzYzY4Mzk0MDIzNjZiMTg5ZGUwZTAxMA==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1708076890'
}
proxies_pool=[
    {'http':'118.195.242.20:8080'},
    {'http':'112.17.16.243:80'},
    {'http':'112.17.16.243	:80 '},
    {'http':'159.226.227.107:80 '},
    {'http':'8.213.137.155	:8080 '},
    {'http':'61.179.129.249	:80 '},
    {'http':'61.179.129.249	:80 '},
    {'http':'140.249.88.102	:80 '},
    {'http':'113.223.215.123:8089 '},
    {'http':'112.17.16.212	:80 '},
    {'http':'112.17.16.229:	80 '},
    {'http':'61.160.202.58	:80 '},
    {'http':'140.249.88.96	:80 '},
    {'http':'61.133.66.69	:9000 '},
    {'http':'112.17.16.236	:80 '},
    {'http':'112.17.16.236	:80 '},
    {'http':'113.223.212.28	:8089 '},
    {'http':'117.57.93.217	:8089 '},
    {'http':'114.231.45.14	:8888'},
    {'https':'125.87.88.234:19961'},
    {'http':'183.236.232.160:8080'},
    {'http':'218.75.69.50:57903'},
    {'http':' 114.231.45.14	:8888'},
    {'http':' 114.231.41.71:8888'},
    {'http':' 47.97.191.179:8018'},
]
url='https://fanyi.baidu.com/v2transapi?'
# url='https://fanyi.baidu.com/v2transapi?'
# 请求参数
data={
    'from': ' zh',
    'to': ' en',
    'query': ' 小猴子',
    'transtype': 'realtime',
    'simple_means_flag': ' 3',
    'sign': ' 320662.1959',
    'token': ' d11820db60854b6ed7014d3118b94803',
    'domain': ' common',
    'ts': ' 1708076890506',
}
proxies=random.choice(proxies_pool)
# 注意，这里与get请求不同，这里的data写data,而get请求则要写params
response=requests.post(url=url,headers=headers,proxies=proxies,data=data)
response.encoding='utf-8'
js_content=response.text
print(js_content)
import json
content=json.loads(js_content)
print(content)

# 在requests中
# post请求不需要编解码
# post请求的参数是data，get请求的参数是paramas
# 不需要请求对象的定制
