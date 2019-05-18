# -*- coding: utf-8 -*-
import scrapy
from crawlerA.items import biliItem
import re



class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']

    llex = 'https://bangumi.bilibili.com/media/web_api/search/result?season_version=-1&area=2&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=3&st=1&sort=0&season_type=1&pagesize=20&page='
    page = 1

    start_urls = [llex+str(page)]

    def parse(self, response):
        # 抽取单media的url
        pat = re.compile('www.bilibili.com/bangumi/play/ss([1-9]\d*)')
        m = pat.findall(response.text)
        for _ in m:
            # href="//www.bilibili.com/bangumi/play/ ss 24588/"
            print(_)
            media_url = 'https://www.bilibili.com/bangumi/media/md'+ _
            yield scrapy.Request(media_url, callback=self.parse_media)

        # 翻页行为
        self.page = self.page + 1
        nexturl = self.llex+str(self.page)
        
        self.logger.info('[索引]下一页 %s x20 ', self.page)
        yield scrapy.Request(nexturl, callback=self.parse)

    def parse_media(self, response):
        bangumi = biliItem()

        bangumi['pageurl'] = response.url
        
        bangumi['img'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[1]/div/img/@src').extract()[0]
        bangumi['title'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/span[1]/text()').extract()[0]
        bangumi['tags'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/span[2]/span/text()').extract()
        bangumi['bigdata'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/text()').extract()[0]
        bangumi['rating'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/text()').extract()[0]
        bangumi['time'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/span[1]/text()').extract()[0]
        bangumi['eps'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/span[2]/text()').extract()[0]
        bangumi['intro'] = response.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[4]/span/text()').extract()[0]

        # 声优演员与staff
        smallbox = response.xpath('//*[@id="app"]/div[2]/div[2]/div/div[2]/div')
        if smallbox:
            # 白页可能
            for onebox in smallbox:
                if '角色' or '声优' in onebox.xpath('//div[1]/text()').extract()[0]:
                    bangumi['cast'] = onebox.xpath('//div[2]/text()').extract()[0]
                elif 'STAFF' in onebox.xpath('//div[1]/text()').extract()[0]:
                    bangumi['staff'] = onebox.xpath('//div[2]/text()').extract()[0]
                else:
                    self.logger.warn('[页面media] %s 标题不合法',bangumi['pageurl'])

        yield bangumi
        self.logger.info('[页面media] 初加工完成 %s | < %s >',bangumi['title'],bangumi['pageurl'])
