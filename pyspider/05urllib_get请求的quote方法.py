# editor: 百年
# time: 2024/2/3 15:33
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6+ <--wd后面跟的是’周杰伦‘的码字
import urllib.request
import urllib.parse

# 需求，获取https://www.baidu.com/s?wd=周杰伦 的网页源码
base_url='https://www.baidu.com/s?wd='
# 要将’周杰伦‘三个字变成unicode编码的格式
# 我们需要urllib.parse()将汉字变成对应的unicode编码
name=urllib.parse.quote('周杰伦')
url=base_url+name

# 模拟浏览器向服务器发送请求
headers={

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 获取响应的内容
response=urllib.request.urlopen(request)
bytes_content=response.read()
content=bytes_content.decode('utf-8')
print(content)
'''
报错:
UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)
'''
# 所以我们不能直接用wd=周杰伦，所以要利用urllib.request.get.quote()
