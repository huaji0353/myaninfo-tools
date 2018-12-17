#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.cnblogs.com/coder2012/p/4990834.html yield是个啥？
"""
bgmtv scrapy
"""
import scrapy
from bgmtv.items import AnimeItem, CharaItem

class BgmtvSpider(scrapy.Spider):
    name = "bgmtv"
    domain = "https://bgm.tv"

    index_url = "https://bgm.tv/anime/browser/airtime/%s-%s"
    index_start_year = 1990
    index_start_month = 1
    
    index_end_year = 1990
    index_end_month = 2

    def _get_index_url(self):
        url = index_url.format(self.year, self.month)
        if self.month > 12:
            self.year = self.year + 1
            self.month = 1
        else:
            self.month = self.month + 1
        return url
        
    def start_requests(self):
        self.year = index_start_year
        self.month = index_start_month
        yield scrapy.Request(url=_get_index_url(), callback=self.parse_index_numpage)

    def parse_index_numpage(self, response):
        if '››' in response.xpath('//a[contains(@class,"p")]/text()').extract(): # 存在下一页
            yield scrapy.Request(url=, callback=self.parse_index_numpage)
        else:
            yield scrapy.Request(url=_get_index_url(), callback=self.parse_index_numpage)
        
    def parse_index(self, response):
        hrefs = response.xpath('//a[contains(@class,"subjectCover")]/@href').extract()
        for href in hrefs:
            yield scrapy.Request(url=domain+href, callback=self.parse_subject)
                
    def parse_subject(self, response):
        item = BgmtvItem()
        yield item

    def parse_character(self, response):
        pass
        