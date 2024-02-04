# editor: 百年
# time: 2024/2/3 14:46
'''
请求对象的定制
'''
import urllib.request

url='https://www.baidu.com'

# url的组成
# 涉及到计算机网络的内容
# 协议://目标主机的域名 :端口号
# 细分
# 协议://权限域名.二级域名.顶级域名 :端口号

# 协议            主机              端口号     路径       参数             锚点
# http/https  www.baidu.com     80/443        s       wd='周杰伦'
'''
几个常用的端口号
http 80
https 443
mysql 3306
oracle 1521
redis 6379
mongodb 27017
'''
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'

}
# 请求对象的定制，因为urlopen方法中不能存储字典，所以headers不能传递进去
# 因为参数顺序的问题，所以Request()不能用位置传参，而需要关键字传参
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
bytes_content=response.read()
content=bytes_content.decode('utf-8')
print(content)
'''
<html>
<head>
	<script>
		location.replace(location.href.replace("https://","http://"));
	</script>
</head>
<body>
	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
</body>
</html>
'''
# 我们发现内容很少，并不是之前那样的，这是因为遇到了反爬,所以要构造请求头


# 再次运行
# 不粘贴了，成功了