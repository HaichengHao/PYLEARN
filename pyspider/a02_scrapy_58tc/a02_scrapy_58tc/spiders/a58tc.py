import scrapy
class A58tcSpider(scrapy.Spider):
    name = "58tc"
    allowed_domains = ["https://jiaozuo.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"]
    start_urls = ["https://jiaozuo.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"]


    def parse(self, response):
    #     # content=response.text
    #     # 注意，之前获取二进制则为response.content
    #     # 而在scrapy之中，则为response.body
    #     # bi_content=response.body
    #     # print('=========下面是网页源码=======')
    #     # print(content)
    #     # print('-------------二进制文件-----------------')
    #     # print(bi_content)
    #     # 如果用xpath不需要再声明tree=etree.HTML(content)
    #     # 而是直接response.xpath(xpath路径)
        span=response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print('===============')
        print(span.extract())
