#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
module docs
"""
import json
from model.anime import Anime
from lxml import etree
from io import StringIO
from mongoengine import *

def get_data(filename):
    json_data = []


    with open('bgmtv.json', 'r') as f:
        for cnt, line in enumerate(f):
            try:
                line = line.strip('\n').strip(',')
                json_obj = json.loads(line)
                json_data.append(json_obj)
            except Exception as e:
                print(e)
                continue
    return json_data

def save_model(data):
    tagdata = data['tagdata']
    tagdict = {}
    for tag in tagdata:
        tree = etree.parse(StringIO(tag))
        all = tree.xpath("//text()")
        key = all[0].strip(":").strip().replace(".", "\u002E").replace("$", " ")
        value = "".join(all[1:])
        tagdict[key] = value
    data['tagdata'] = tagdict
    data['cover'] = data['cover'][0] if len(data['cover']) else ''
    data.pop("like")
    return Anime(**data)

connect('test')
data = get_data("bgmtv.json")
for _ in data:
    model = save_model(_)
    try:
        model.save()
    except ValidationError as e:
        print(model.tagdata)
        continue


