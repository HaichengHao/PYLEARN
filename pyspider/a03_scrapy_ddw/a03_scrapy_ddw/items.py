# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class A03ScrapyDdwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # //a/img/@src 《--图片
    # //p[@class="name"]/a/@title 《--书名
    # //p[@class="price"]/span[1] 《--价格

    # 图片链接
    src= scrapy.Field()
    # 名称
    name=scrapy.Field()
    # 价格
    price=scrapy.Field()

