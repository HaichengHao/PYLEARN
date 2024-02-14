# editor: 百年
# time: 2024/2/13 16:33
'''
selenium 是一个用于web应用程序测试的工具
selenium 测试直接运行在浏览器中，就像真的用户在操作一样
selenium 也是支持无界面浏览器操作的


为什么使用selenium? 模拟浏览器功能，自动执行网页中的js代码，实现动态加载

如何安装selenium？
1) 操作谷歌浏览器驱动下载
2) 谷歌驱动和谷歌浏览器不同版本之间的映射表
3) 查看谷歌浏览器版本
4) pip install selenium

selenium 的使用步骤
1)导入: from selenium import webdriver
2)创建谷歌浏览器操作对象
    path=谷歌浏览器驱动文件路径
    browser=webdriver.Chrom(path)
3)访问地址
    url=要访问的url
    browser.get(url)
'''


# 如果使用的selenium新，则使用注释方案
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 尝试传参
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get('https://www.baidu.com/')
driver.quit() 
'''

# 旧版本
# 1导包
from selenium import webdriver
# 2设定chromedriver的路径，
path="chromedriver.exe"
# 3创建浏览器操作对象
browser=webdriver.Chrome(path)

# 4访问网站
# url='https://www.jd.com/'

url='https://www.jd.com/'
browser.get(url)
# 利用.page_source方法获取网页源码
content=browser.page_source
print(content)


