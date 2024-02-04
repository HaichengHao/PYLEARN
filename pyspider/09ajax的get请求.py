# editor: 百年
# time: 2024/2/3 20:07
# get请求获取豆瓣电影第一页的数据并保存
import urllib.request
import urllib.parse
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
# 响应对象的接收
response=urllib.request.urlopen(request)
# 返回数据的解码
content=response.read().decode('utf-8')
print(content)

# 数据下载到本地
# open方法默认使用的是gbk的编码，如果我们要想保存汉字，那么要在open()方法中指定字符集
with open('.\douban.json','a+',encoding='utf-8') as wfp:
    wfp.write(content)
#     获取到的如果只在一行的话按ctrl+alt+l可以实现换行（自动）
