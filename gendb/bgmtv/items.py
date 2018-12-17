# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# TODOTDO
anime_base = {
    "name": {"zh": "", "jp": "", "nhg": "", "en": ""},  # 名字 中文 日语 罗马音 英语
    "cover": None,  # 封面(base64/blob/url)
    "time": [2000, 10],  # 放送开始(yy/mm)
    "episodes": 13,  # 话数
    "staff": {},  # staff
    "baseinfos": {},  # 一些基本信息
    "story": "",  # 故事简介
    "tags":  # 标签
    {
        "genre": [],  # 类型
        "label": {},  # bgmtv的标注数据
    },
    "ranking": {},  # 评分
    "cast": {},  # 角色
    "relate":  # 相关
    {
        "bgm": [],  # 音乐
        "series": [],  # 系列
        "recommend": [],  # 相关推荐
    },
    "origin": {},  # 引用来源请注名
}

chara_base = {
    "name": {"zh": "", "jp": "", "nhg": "", "en": ""},  # 名字 中文 日语 罗马音 英语
    "sex": 0,  # 妹子0/汉子1
    "picture": None,  # 截图(base64/blob/url)
    "tags":  # 标签
    {
        "cv": "",  # 声优
        "label": [],  # 给角色打标签
    },
    "relate":  # 相关
    {
        "acted": [],  # 出演
        "similar": [],  # 类似角色
    },
    "origin": {},  # 引用来源请注名
}


class baseNameItem(scrapy.Item):
    zh = scrapy.Field() # 中文
    jp = scrapy.Field() # 日语
    en = scrapy.Field() # 英语
    nhg = scrapy.Field() # 罗马音

class basePicItem(scrapy.Item):
    url = scrapy.Field()
    blob = scrapy.Field()
    base64 = scrapy.Field()

class baseTimeItem(scrapy.Item):
    year = scrapy.Field()
    month = scrapy.Field()

class exbaseObjItem(scrapy.Item):
    origin = scrapy.Field()
    
class exbaseManItem(exbaseObjItem, scrapy.Item):
    uid = scrapy.Field()
    sex = scrapy.Field()
    pic = scrapy.Field()

class StaffItem(exbaseManItem):
    studio = scrapy.Field()
    
class CharaItem(exbaseManItem):
    tags = scrapy.Field()
    cv = scrapy.Field()
    
class AnimeItem(exbaseObjItem):
    uid = scrapy.Field()
    name = scrapy.Field()
    start_time = scrapy.Field()
    cover = scrapy.Field()
    episodes = scrapy.Field()
    staffs = scrapy.Field()
    genre = scrapy.Field()
    chara = scrapy.Field()
    story = scrapy.Field()
    label = scrapy.Field()
    ranking = scrapy.Field()
