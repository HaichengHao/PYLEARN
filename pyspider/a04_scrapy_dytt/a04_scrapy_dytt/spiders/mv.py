import scrapy


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["https://www.btwuji.com/html/gndy/china/index.html"]
    start_urls = ["https://www.btwuji.com/html/gndy/china/index.html"]

    def parse(self, response):
        print('--------------')
