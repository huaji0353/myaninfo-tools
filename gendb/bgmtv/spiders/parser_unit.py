# -*- coding:utf-8 -*-
# https://www.cnblogs.com/ywk-1994/p/9543360.html
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
from bs4 import BeautifulSoup
import bgmtv.dataformat as dataformat # item的导入 TODO
import copy

# 实现一个空路由表，利用装饰器将url和功能函数的对应关系自动存到这个字典中
url_router_dict = {}

# 定义一个装饰器
# 再给一层函数定义，用来传入一个参数,这个参数就是访问的页面地址
# @decorator  # index = decorator(index)
def url_router_wrap(url):
    def decorator(parser):
        def wrapper(*args, **kwargs):
            parser(*args, **kwargs)
        url_router_dict[url] = wrapper  # 既可以是parser也可以是wrapper,单如果是parser,就无法添加wrapper中的新功能
        return wrapper
    return decorator

@url_router_wrap('https://bgm.tv/anime/browser/airtime/')
def bgmtv_index(Spider, index_page):
    return {'test':1}

@url_router_wrap('https://bgm.tv/subject/')
def bgmtv_subject(Spider, subject_page):
    '''bs4解析页面，提取内容，填充字典，返回字典'''
    soup = BeautifulSoup(subject_page, 'lxml')

    subject_data = copy.deepcopy(dataformat.anime_base)

    # 头内容
    headerSubject = soup.find('h1', 'nameSingle')
    subject_data['name']['jp'] = headerSubject.a.text
    subject_data['name']['zh'] = headerSubject.a['title']
    subject_data['origin']['bgmtv'] = 'https://bgm.tv'+headerSubject.a['href']
    subject_data['tags']['genre'] = headerSubject.small.text

    mainWrapper = soup.find('div', 'mainWrapper')

    # 左上内容
    columnSubjectHomeA = mainWrapper.find('div', 'infobox')
    # 是否下载？TODO
    subject_data['cover'] = 'https:'+columnSubjectHomeA.div.a['href']
    baseinfos = columnSubjectHomeA.ul.select('li')
    for baseinfo in baseinfos:
        # 清洗数据！TODO
        if not isinstance(baseinfo.contents[1], str):
            # 不是文本是超链接的情况
            subject_data['baseinfos'][
                baseinfo.contents[0].text[: -2]] = baseinfo.contents[1].text
        else:
            # 去掉":"的干扰 然后按索引写字典
            subject_data['baseinfos'][
                baseinfo.contents[0].text[: -2]] = baseinfo.contents[1]

    columnSubjectHomeB = mainWrapper.find(id='columnSubjectHomeB')
    # 右上内容
    subject_data['story'] = columnSubjectHomeB.find(id='subject_summary').text
    tags = columnSubjectHomeB.find(
        'div', 'subject_tag_section').div.select('a')
    for tag in tags:
        # 清洗数据！TODO
        subject_data['tags']['label'][tag.span.text] = (
            'https://bgm.tv'+tag['href'], int(tag.small.text))
    subject_data['ranking']['bgmtv'] = float(
        columnSubjectHomeB.find('span', 'number').text)

    # 右下内容
    # 加入/characters模版，提取另附 TODO
    relates = columnSubjectHomeB.find('div', 'content_inner').select('li')
    for relate in relates:
        pass

    return subject_data
