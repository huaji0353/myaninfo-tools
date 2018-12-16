# -*- coding:utf-8 -*-
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
from bs4 import BeautifulSoup
import dataformat
import copy


def bangumi_subject_parser(subject_page):
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


if __name__ == '__main__':
    with open('6007.html', 'rb') as f:
        dic = bangumi_subject_parser(f.read())
    0/0
