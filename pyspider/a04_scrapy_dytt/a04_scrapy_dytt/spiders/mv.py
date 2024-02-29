import scrapy
from a04_scrapy_dytt.items import A04ScrapyDyttItem
class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["www.tlyya.com"]
    start_urls = ["https://www.tlyya.com/movie/0-2-0-1-1.html"]

    base_url="https://www.tlyya.com/movie/0-2-0-1-"
    page=1
    def parse(self, response):
        # //li/div/a/@data-original <--图片链接
        # //li/div/a/@title/text() <--电影名称
        # //div[@class="stui-vodlist__detail"]/h4/a/@href 《--二级块跳转链接
        # //a/img/@data-original  <--跳转之后的页面的图片数据源
        # print('------测试用--------')
        a_lst=response.xpath('//div/h4/a')
        # name_lst=response.xpath('//div/h4/a/@title').extract()
        # detail_page=response.xpath('//div[@class="stui-vodlist__detail"]/h4/a/@href').extract_first()
        # print(name_lst)
        for a in a_lst:
            name=a.xpath('./@title').extract_first()
            detail_page=a.xpath('./@href').extract_first()
            # print(name_lst)
            # print(detail_page)

#             开始构造对详情页的请求
            yield scrapy.Request(url=detail_page,callback=self.parse_detail,meta={'name':name})
    #            利用meta可以将name属性传给二级页将电影海报和电影名称组成一个字典
        if self.page<3: #<--爬取前两页
            self.page+=1
            url=self.base_url+str(self.page)+'.html'
            yield scrapy.Request(url=url,callback=self.parse)


    # 自定义对详情页的请求方法
    def parse_detail(self,response):
        # print('===测试用=======')
        pic_src=response.xpath('//a/img/@data-original').extract_first()
        # print(pic_src)
        name=response.meta['name']

        # 生成对象 -电影
        movie=A04ScrapyDyttItem(name=name,src=pic_src)
        yield movie
