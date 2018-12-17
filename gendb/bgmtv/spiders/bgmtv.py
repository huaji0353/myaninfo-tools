#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.cnblogs.com/coder2012/p/4990834.html yield是个生成器
# https://www.cnblogs.com/huwei934/p/6970951.html scrapy机制
"""
bgmtv scrapy
"""
import scrapy
from bgmtv.items import AnimeItem, CharaItem, baseNameItem, basePicItem

domain = "https://bgm.tv"

index_start_year = 1990
index_start_month = 1 # 从此开始

index_end_year = 1990
index_end_month = 3 # 不到此值

# ref https://github.com/AllenTom/BangumiSpider/blob/master/bangumi/spiders/bangumi_animate.py
def index0(selector, index=0):
    return selector[index] if len(selector) != 0 else None

class BgmtvSpider(scrapy.Spider):
    name = "bgmtv"

    def _get_index_url(self):
        url = "https://bgm.tv/anime/browser/airtime/%s-%s"%(self.year, self.month)
        if self.month >= 12:
            if self.year >= index_end_year:
                return
            self.year = self.year + 1
            self.month = 1
        else:
            if self.month >= index_end_month:
                return
            self.month = self.month + 1
        return url
        
    def start_requests(self):
        ''' 启动爬虫时只调用一次的函数 '''
        self.year = index_start_year
        self.month = index_start_month
        yield scrapy.Request(url=self._get_index_url(), callback=self.parse)

    # https://bgm.tv/anime/browser/airtime/2006-1
    def parse(self, response):
        ''' 外边有个循环地请求这个函数 并收集yield返回的 Request Item 实例'''
        # 存在下一页 -> 解析此页中的url 下一页
        # 不存在下一页 -> 解析此页中的url 下一个月份
        pagenum = response.xpath('//a[contains(@class,"p")]/text()').extract()
        if '››' in pagenum: # 存在下一页
            yield scrapy.Request(url=response.url+pagenum[1], callback=self.parse)
        else:
            url = self._get_index_url()
            # 日期达到end情况
            if url:
                yield scrapy.Request(url=url, callback=self.parse)
        hrefs = response.xpath('//a[contains(@class,"subjectCover")]/@href').extract()
        for href in hrefs:
            yield scrapy.Request(url=domain+href, callback=self.parse_subject)
            
    # https://bgm.tv/subject/135275
    def parse_subject(self, response):
        if index0(response.xpath('//*[@id="colunmNotice"]/div/p[1]/text()').extract()):
            # 404 可能爬到了里区...
            return 
        anime = AnimeItem()
        name = baseNameItem()
        pic = basePicItem()
        anime['origin'] = domain+index0(response.xpath('//*[@id="headerSubject"]/h1/a/@href').extract())
        name['jp'] = index0(response.xpath('//*[@id="headerSubject"]/h1/a/text()').extract())
        pic['url'] = 'https:'+index0(response.xpath('//*[@id="bangumiInfo"]/div/div/a/@href').extract())
        anime['name'] = name
        anime['cover'] = pic
        yield anime

    def parse_character(self, response):
        pass
        