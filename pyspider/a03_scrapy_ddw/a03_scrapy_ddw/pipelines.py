# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道需要先在settings里开启管道
class A03ScrapyDdwPipeline:
    # 在爬虫文件开始之前就执行的一个方法
    def open_spider(self,spider):
        print('++++++++++++++++++++++++++')
    # 在爬虫文件开始之前就打开一个对象
        self.fp = open('books.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        # item就是我们在自己的爬虫文件中定义的yiled后面(本案例中是book)的对象的形参
        # 注意 write 方法必须写一个字符串而不是其它对象，所以要转成字符串
        # 还有记得用a模式，如果用w则会覆写，拿一个覆写一次，到最后只会剩最后一个的信息

        # 以下模式并不推荐，因为对文件打开关闭过于频繁
        # with open('./ddbook.json','a+',encoding='utf-8')as wfp:
        #     wfp.write(str(item))

        self.fp.write(str(item))


        return item
    # 在爬虫文件执行之后执行的方法
    def close_spider(self,spider):
        print('--------------')
        self.fp.close()


# 多条管道同时开启
# 1定义管道类
# 2在settings里开启多管道

import urllib.request
class DangpicDownloadPipeline:
    def process_item(self, item, spider):
        picurl=item.get('src')
        filename='./bookpic/'+item.get('name')+'.jpg'
        urllib.request.urlretrieve(url=picurl,filename=filename)

        return item
