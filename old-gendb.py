#coding=utf8
import os

import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

bangumi_format = [
    ("cover", "[img]{}[/img]\n\n"),
    ("story", "[b]Story: [/b]\n\n{}\n\n"),
    ("staff", "[b]Staff: [/b]\n\n{}\n\n"),
    ("cast", "[b]Cast: [/b]\n\n{}\n\n"),
    ("alt", "(来源于 {} )\n")
]

#设置User-Agent
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
}


def fu(url):
	'''requests抓取链接页面'''
	try:
		return requests.get(url,headers=headers)
	except:
		print("process(): "+url)
	
def deu(page):
	'''BeautifulSoup分析页面，抓取需求内容，返回格式化语句'''
	soup = BeautifulSoup(page.content,'lxml')
	try:
		#print(item.contents)
		#用beautifulsoup抓取出想要的数据
		
		# 作品名
		name = soup.select('.nameSingle a')[0].get_text()
		# 类型
		broadcast_type = soup.select('.nameSingle small')[0].get_text()
		# 评分
		score = soup.select('.global_score .number')[0].get_text()
		# 标签
		tags = soup.select('.subject_tag_section .inner a')
		tag_list = []
		for tag in tags:
			tag_name = tag.find('span')
			tag_num = tag.find('small')
			tag_list.append((tag_name.get_text(), tag_num.get_text()))
		# staff
		dic = {}
		nodes = soup.select('#infobox li')
		for node in nodes:
			t = node.select('.tip')[0].get_text()

			if t == '中文名: ':
				# print(t+" get")
				dic['中文名'] = node.get_text().strip(t)

			elif t == '导演: ':
				# print(t+" get")
				dic['导演'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '总导演: ':
				# print(t+" get")
				dic['总导演'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '副导演: ':
				# print(t+" get")
				dic['副导演'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '放送开始: ' or t == '发售日: ' or t == '上映年度: ':
				# print(t+" get")
				try:
					convert_date = datetime.datetime.strptime(node.get_text().strip(t), "%Y年%m月%d日").date()
				except Exception as e:
					convert_date = datetime.datetime.now().date()

				dic['播放日期'] = convert_date

			elif t == '系列构成: ':
				# print(t+" get")
				dic['系列构成'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '动画制作: ':
				# print(t+" get")
				dic['动画制作'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '脚本: ':
				# print(t+" get")
				dic['脚本'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '分镜: ':
				# print(t+" get")
				dic['分镜'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '演出: ':
				# print(t+" get")
				dic['演出'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '作画监督: ':
				# print(t+" get")
				dic['作画监督'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '原画: ':
				# print(t+" get")
				dic['原画'] = ','.join([person.get_text() for person in node.select('a')])

			elif t == '制片人: ':
				# print(t+" get")
				dic['制片人'] = ','.join([person.get_text() for person in node.select('a')])


		#把抓取的数据保存到元组中
		lesson_data = {"lesson_name":lesson_name,"lesson_url":lesson_url,"lesson_content":lesson_content,"lesson_stu":lesson_stu,"lesson_time":lesson_time,"lesson_level":lesson_level}
		sql = "insert into lesson(id,lesson_name,lesson_url,lesson_content,lesson_stu,lesson_time,lesson_level) values(null,'%s','%s','%s','%s','%s','%s')"%(name,url,cont,stu,time,level)
		return sql
	except:
		pass

def exu(sql):
	'''sql3数据库'''
	cur = conn.cursor()
	cur.execute(sql)
	conn.commit()
	
def process(url, thread_id):
	#爬虫的原始链接BaseUrl
	print("[start]process(%s, %s)"%(url, thread_id))

	page = fu(url)
	sql = deu(page)
	exu(sql)
	
	print("[done]process(%s, %s)"%(url, thread_id))

if __name__ == '__main__':
    #获取当前文件的绝对路径
    BASE_DIR = os.path.dirname(__file__)
    #链接数据库sqlite3
    conn = sqlite3.connect(os.path.join(BASE_DIR,'bangumi.db'))
    
    starttime = datetime.datetime.now()
    process("https://bgm.tv/subject/135275", 1)
    endtime = datetime.datetime.now()
    conn.close()
    print("爬取%d页用时："%PAGE_NUM,(endtime-starttime).seconds,"s")
