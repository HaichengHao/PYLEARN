import scrapy


class AutohomeSpider(scrapy.Spider):
    name = "autohome"
    allowed_domains = ["https://car.autohome.com.cn/price/brand-15.html"]
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        car_info=response.xpath('//div[@class="main-title"]/a/text()')
        price_info=response.xpath('//span[@class="font-arial"]/text()')
        # print(price_info)
        # print(car_info)
        car_type=[]
        car_price=[]
        car_data=[]
        for car in car_info:
            car_type.append(car.extract())
        for price in price_info:
            car_price.append(price.extract())
        print(car_type,car_price)
        for i in range(0,len(car_type)):
            data_s='{'+'\''+car_type[i]+'\''+':'+'\''+car_price[i]+'\''+'}'
            # print(data_s)
            car_data.append(data_s)
        print(car_data)