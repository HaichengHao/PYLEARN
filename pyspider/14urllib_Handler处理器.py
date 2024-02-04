# editor: 百年
# time: 2024/2/4 17:21
'''
适用handler访问百度，获取百度网页源码
'''
import urllib.request

url='http://www.baidu.com'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
# 1 .HTTPhandler()   2 .build_opener()   3 opener.open(request)

# 1获取handler对象
handler=urllib.request.HTTPHandler()
# 2 获取opener对象
opener=urllib.request.build_opener(handler)
# 3 调用open()方法
response=opener.open(request)
content=response.read().decode('utf-8')
print(content)