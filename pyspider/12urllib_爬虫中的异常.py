# editor: 百年
# time: 2024/2/4 15:40
'''
爬虫中的异常 URLError\HTTPError
1.HTTPError类是URLError类的子类
2.导入的包urllib.error.HTTPError  urllib.error.URLError
3.http错误:http错误是针对浏览器无法连接到服务器而增加出来的错误提示，
4.通过urllib发送请求的时候，有可能会发送失败，这个时候如果想让代码更健壮，可以通过异常处理捕获异常
'''
# https://blog.csdn.net/bsegebr/article/details/123255129
import urllib.request
import urllib.error
# url='https://blog.csdn.net/bsegebr/article/details/123255129'
# url='https://blog.csdn.net/bsegebr/article/details/1232551291' #<--这个用于演示urllib.error.HTTPError
url='https://www.goudandouban.com' # <--这个统一资源定位符用于演示urllib.error.URLError
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
try:
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError as e:
    print(e)
except urllib.error.URLError as e:
    print(e)
