import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from b01_scrapy_crawlspider_dsw.items import B01ScrapyCrawlspiderDswItem

class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    # 注意，首页数据可能会被漏掉，所以要看到第一页的链接
    start_urls = ["https://www.dushu.com/book/1181_1.html"]
    # LinkExtractor(allow=r"/book/1181_\d+\.html")
    rules = (
        Rule(LinkExtractor(allow=r"/book/1181_\d+\.html"),
                callback="parse_item",follow=True),
    )

    def parse_item(self, response):
        img_lst=response.xpath('//div[@class="bookslist"]/ul/li/div/div/a/img')
        for img in img_lst:
            bookname=img.xpath('./@alt').extract_first()
            booksrc=img.xpath('./@data-original').extract_first()
            print(bookname,'\n',booksrc)
            book = B01ScrapyCrawlspiderDswItem(name=bookname,src=booksrc)
            yield book
            # print()
        # return item
