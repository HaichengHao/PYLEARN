import scrapy


class BaiduinfoSpider(scrapy.Spider):
    # 爬虫的名字，一般用于运行爬虫的时候使用的值
    name = "baiduinfo"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始url 即第一次要访问的域名
    #     start_urls 是在allowed_domains 的前面加一个http://
    #                                       在后面加一个/
    start_urls = ["http://www.baidu.com/"]

    #是执行了start_urls之后执行的方法  方法中的response 就是返回的那个对象
    # 相当于response=urllib.request.urlopen()
    # 也相当于requests 中的response=requests.get()
    def parse(self, response):
        print('子非我，安知我不知鱼之乐')

