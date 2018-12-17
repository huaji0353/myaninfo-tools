#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
bgmtv scrapy
"""
import scrapy
from . import parser_unit

from multiprocessing import Process, Queue

class BgmtvSpider(scrapy.Spider):
    name = "bgmtv"
    allowed_domains = ['bgm.tv']

    start_urls = "https://bgm.tv/anime/browser/airtime/1990-1"

    def start_requests(self):
        self.url_queue = Queue()
        self.url_queue.put("https://bgm.tv/anime/browser/airtime/1990-1")
        while 1:
            url = self.url_queue.get()
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ''' 通过传入访问地址，获取对应的功能函数 '''
        url = response.url
        urldir = '/'.join(url.strip().split('/')[:-1])+"/"
        try:
            parser = parser_unit.url_router_dict[urldir] # 路由表升级TODO
            yield parser(self, response.text)
        except KeyError:
             pass
