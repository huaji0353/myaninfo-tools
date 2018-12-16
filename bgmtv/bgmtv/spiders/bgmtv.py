#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
bgmtv scrapy
"""
import scrapy
from bgmtv.items import BgmtvItem


class BgmtvSpider(scrapy.Spider):
    name = "bgmtv"

    allowed_domains = ['bgm.tv']


    start_id = 1
    end_id = 2600

    url = "http://bgm.tv/subject/"

    def start_requests(self):
        urls = [
            self.url+str(url_id) for url_id in range(self.start_id, self.end_id)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        if response.xpath(
                '//title/text()').extract_first().split("|")[0] == "坟场":
            return self.gen_url(response)
        item = BgmtvItem()
        item['desc'] = "".join(
            response.xpath('//div[@id="subject_summary"]/text()').extract())
        item['title'] = response.xpath(
            '//title/text()').extract_first().split("|")[0]
        item['tag'] = response.xpath(
            '//div[@class="inner"]/a[@class="l"]/span/text()').extract()
        item['rank'] = response.xpath(
            '//span[@property="v:average"]/text()').extract_first()
        item['comment'] = response.xpath(
            '//div[@class="text_main_even"]/div/p/text()').extract()
        item['cover'] = response.xpath('//img[@class="cover"]/@src').extract()
        item['like'] = [
            url.split("/")[-1]
            for url in response.xpath(
                '//li[@class="clearit"]/a[@class="avatar thumbTip"]/@href').extract()]
        item['tagdata'] = response.xpath('//ul[@id="infobox"]/li').extract() 
        yield item


