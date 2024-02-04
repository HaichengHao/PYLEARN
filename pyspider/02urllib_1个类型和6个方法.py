# editor: 百年
# time: 2024/2/2 11:53
'''

'''

# 导入urllib包的request
import urllib.request
base_url='http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(base_url)
# 一个类型和六个方法
print(type(response))
# <class 'http.client.HTTPResponse'>
# 类型为 HTTPResponse 即超文本传输协议响应类型

# 1.read([size])默认按照一字节一字节读，如果指定size,则按指定的size字节读
'''bytes_content=response.read()
content=bytes_content.decode('utf-8')'''

# 2.readline()默认读取一行，详情查看pylearn相关内容
'''content=response.readline().decode('utf-8')
print(content)'''

# 3.readlines()读取多行
'''content=response.readlines()'''


'''print(type(content))'''
# <class 'list'> <--可以发现，readlines()方法会把读取到的内容放入列表当中保存

# 4.getcode()方法返回状态码，如果状态码是200表示无错误
'''print(response.getcode())
'''
# 200

# 5.geturl()获取url
'''print(response.geturl())'''
# http://www.baidu.com

# 6.getheaders() 获取状态信息和请求头
print(response.getheaders())
# [('Content-Length', '405659'), ('Content-Security-Policy', "frame-ancestors 'self' https://chat.baidu.com http://mirror-chat.baidu.com https://fj-chat.baidu.com https://hba-chat.baidu.com https://hbe-chat.baidu.com https://njjs-chat.baidu.com https://nj-chat.baidu.com https://hna-chat.baidu.com https://hnb-chat.baidu.com http://debug.baidu-int.com;"), ('Content-Type', 'text/html; charset=utf-8'), ('Date', 'Fri, 02 Feb 2024 09:16:28 GMT'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('Server', 'BWS/1.1'), ('Set-Cookie', 'BAIDUID=BEBF46F02225FAF487C997D012C0ACE7:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'BIDUPSID=BEBF46F02225FAF487C997D012C0ACE7; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'PSTM=1706865388; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'BAIDUID=BEBF46F02225FAF4FAFA271772F98FF5:FG=1; max-age=31536000; expires=Sat, 01-Feb-25 09:16:28 GMT; domain=.baidu.com; path=/; version=1; comment=bd'), ('Traceid', '1706865388284982554612561742492745423344'), ('Vary', 'Accept-Encoding'), ('X-Ua-Compatible', 'IE=Edge,chrome=1'), ('X-Xss-Protection', '1;mode=block'), ('Connection', 'close')]
