# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BgmtvItem(scrapy.Item):
    # define the fields for your item here like:
#    sale_day = scrapy.Field()
#    isbn = scrapy.Field()
#    author = scrapy.Field()
#    Publish = scrapy.Field()
    tagdata = scrapy.Field()
    desc = scrapy.Field()
    rank = scrapy.Field()
    tag = scrapy.Field()
    comment = scrapy.Field()
    like = scrapy.Field()
    cover = scrapy.Field()
    title = scrapy.Field()

