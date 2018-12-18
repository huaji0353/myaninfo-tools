# scrapy学习
启动爬虫后从scrapy.Spider start_requests()或start_urls作为起始

从def parse(self, response): 生成实例 - 实例工厂

yield scrapy.Request(url, callback=self.some_parse)

yield scrapy.Item

# TODO
把数据格式制定好，然后编写数据库代码

编写更多的parser....更多....更多...