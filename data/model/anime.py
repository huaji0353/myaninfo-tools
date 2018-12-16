#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
module docs
"""
from mongoengine import *

class Anime(Document):
    title = StringField(required=True, max_length=200)
    desc = StringField()
    tag = ListField(StringField(max_length=50))
    rank = FloatField()
    comment = ListField(StringField(max_length=200))
    cover = StringField()
    tagdata = DictField()


