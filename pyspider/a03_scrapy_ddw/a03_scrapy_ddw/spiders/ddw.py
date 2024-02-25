import scrapy
from a03_scrapy_ddw.items import A03ScrapyDdwItem

class DdwSpider(scrapy.Spider):
    name = "ddw"
    # 注意如果是多页下载的话一定要修改允许的域名范围
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/pg1-cp01.03.41.00.00.00.html"]


    base_url='http://category.dangdang.com/pg'
    page=1
    def parse(self, response):
        # 开启pipline 进行数据下载
        # items 用来定义数据结构（即要下载的数据都有什么）
        # //ul[@class="bigimg"]/li/a/img/@src 《--图片
        # //ul[@class="bigimg"]/li/a/img/@alt
        # //ul[@class="bigimg"]/li/p[@class="price"]/span[1]/text()《--价格
        # img_src=response.xpath('//a/img/@src')
        # name=response.xpath('//ul[@class="bigimg"]/li/a/img/@alt')
        # price=response.xpath('//p[@class="price"]/span[1]/text')
        # print(img_src)
        # print(name)
        # print(price)


        # 所有的selector 对象都可以再次调用xpath方法
        # 注意，在当前selector对象的基础上再加上之后的路径
        li_list=response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # print(li)
            # 注意,scrapy中xpath返回的是selector对象列表，而我们要的是selector对象data的属性值，所以要使用.extract_first()提取属性值
            src = li.xpath('.//img/@data-original').extract_first() #相当于//ul[@class="bigimg"]/li + //img/@src

            # 第一张图片和其他的图片的标签的属性是不一样的
            # 第一张图片的src是可以使用的  其他的图片的地址是data-original
            if src: #如果是li.xpath('.//img/@data-original').extract_first() 即如果不为空值None
                src = 'http:'+src #那就保持不变(并拼接上协议)
            else: #如果为空
                # /img/@src
                src = 'http:'+li.xpath('.//img/@src').extract_first() #那就新定义一个访问到src
            name=li.xpath('.//img/@alt').extract_first()#相当于//ul[@class="bigimg"]/li + //img/@alt
            price=li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            # print(src,name,price)
            # 注意要实现下面这行代码就得先去items.py中定义数据格式
            # 创建一个book对象并调用items.py中的A03ScrapyDdwItem类方法
            book=A03ScrapyDdwItem(src=src,name=name,price=price)
#             拿到这些个对象后要交给pipelines.py去下载
# 如何交给piplines下载? 利用yiled
# 为什么?  因为带有yiled的函数不再是一个普通的函数，而是一个生成器generator,可以用于迭代
# yiled是一个类似于return的关键字,迭代一次遇到yiled时就返回yiled后面的值。重点是：下次迭代就从这个位置后开始执行
# 案例 当当网  1 yiled   2 管道封装 3 多管道下载 4 多页数据下载
#             上面的代码中创建了book对象调用items中的方法将其定义
#             每生成book对象就把对象交给piplines
            yield book

#             每一页爬取的业务逻辑都是一样的，只需要再次让每一页的请求调用parse就行
        if self.page<3:
            self.page+=1
            url=self.base_url+str(self.page)+'-cp01.03.41.00.00.00.html'

            # 难点在于如何调用parse方法
            # scrapy.Request就是Scrapy 的 get请求
            # url 就是请求地址
            # callback就是要执行的那个函数，注意不允许加'()'
            # 核心是递归调用了parse方法
            yield scrapy.Request(url=url,callback=self.parse)