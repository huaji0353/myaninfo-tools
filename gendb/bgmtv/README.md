# crapy学习
启动爬虫后从scrapy.Spider start_requests()或start_urls作为起始
启动下载器进行Request
def parse(self, response): 解析
yield scrapy.Request(url, callback=self.some_parse) 将url放入队列
yield item 返回item