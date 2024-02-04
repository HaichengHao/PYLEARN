# editor: 百年
# time: 2024/2/3 16:05
# 应用场景：多个参数的时候
# https://www.baidu.com/s?wd=周杰伦&gender=男&location=中国台湾省
import random
import urllib.request
import urllib.parse #导入urllib包的parse(解析)模块
# 代理池
proxies_pool = [
    {'http': '183.221.242.103:9443'},
    {'http': '183.230.198.80:9091'},
    {'http': '183.221.242.103:9443'},
    {'http': '183.230.198.80:9091'},
    {'http': '183.172.197.188:4780'},
    {'http': '183.173.178.231:4780'},
    {'http': '183.172.169.225:4780'},
    {'http': '188.132.221.27:8080'},
    {'http': '103.152.232.134:8080'},
    {'http': '103.227.252.102:8080'},
    {'http': '79.106.170.34:8989'},
    {'http': '190.110.99.189:999'},
]
my_proxy=random.choice(proxies_pool)
# 多个参数
data={
    'q':'周杰伦'
}
# 利用urllib.parse.urlencode()方法来把汉字转化为unicode编码
encode_data=urllib.parse.urlencode(data)
base_url='https://cn.bing.com/search?'
url=base_url+encode_data
# 构造请求头
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 获取响应的内容
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
with open('./demo2.html','a+',encoding='utf-8') as wf:
    wf.write(content)



