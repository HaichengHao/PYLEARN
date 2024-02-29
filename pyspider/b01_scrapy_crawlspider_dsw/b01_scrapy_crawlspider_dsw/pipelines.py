# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class B01ScrapyCrawlspiderDswPipeline:
    def open_spider(self,spider):
        self.fp=open('books.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    def close_spider(self,spider):
        self.fp.close()

# 可以通过下面的from 加载settings.py的文件配置
from scrapy.utils.project import get_project_settings
class MysqlPipline:
    def open_spider(self,spider):
        settings=get_project_settings()

# DB_HOST="127.0.0.1"
# DB_PORT=3306
# DB_USER='root'
# DB_PASSWORD=''
# DB_NAME=''
# DB_CHARSET='utf-8'
#         注意顺序
        self.host=settings['DB_HOST']
        self.port=settings['DB_PORT']
        self.user=settings['DB_USER']
        self.password=settings['DB_PASSWORD']
        self.name=settings['DB_NAME']
        self.charset=settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor=self.conn.cursor()
    def  process_item(self, item, spider):
        sql = 'insert into book(name,src) values("{}","{}")'.format(item['name'],item['src'])
        #执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
