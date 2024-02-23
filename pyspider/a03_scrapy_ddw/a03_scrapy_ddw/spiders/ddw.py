import scrapy
from a03_scrapy_ddw import A03ScrapyDdwItem

class DdwSpider(scrapy.Spider):
    name = "ddw"
    allowed_domains = ["http://category.dangdang.com/pg1-cp01.03.41.00.00.00.html"]
    start_urls = ["http://category.dangdang.com/pg1-cp01.03.41.00.00.00.html"]

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
        # 注意，在当前selector对象的基础上再加上滞后的路径
        li_list=response.xpath('//ul[@class="bigimg"]/li')
        for li in li_list:
            # print(li)
            # 注意,scrapy中xpath返回的是selector对象列表，而我们要的是selector对象data的属性值，所以要使用.extract_first()提取属性值
            src='https://'+li.xpath('.//a/img/@data-original').extract_first()  #相当于//ul[@class="bigimg"]/li + //a/img/@src
            name=li.xpath('.//a/img/@alt').extract_first()
            price=li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            # print(src,name,price)
            # 注意要实现下面这行代码就得先去items.py中定义数据格式
            book=A03ScrapyDdwItem(src=src,name=name,price=price)
#             拿到这些个对象后要交给pipelines.py去下载
# 如何交给piplines下载? 利用yiled
# 为什么?  因为带有yiled的函数不再是一个普通的函数，而是一个生成器generator,可以用于迭代
# yiled是一个类似于return的关键字,迭代一次遇到yiled时就返回yiled后面开始执行

