## scrapy 工作原理

1. 引擎向spider要url
2. 引擎将要爬取的url给调度器
3. 调度器会将url生成请求对象放入到指定的队列中
4. 调度器从队列中出队一个请求
5. 引擎将请求交给下载器进行处理
6. 下载器发送请求获取互联网数据
7. 下载器将数据返回给引擎
8. 引擎将数据再给到spiders
9. spiders通过xpath解析该数据，得到数据或者url
10. spiders将数据或者url给引擎
11. 引擎判断该数据是数据还是url，是数据，交给管道(item pipline)处理，是url交给调度器处理
![](D:\PYWORK\pyspider\carhome\scrapy工作原理示意图.png)