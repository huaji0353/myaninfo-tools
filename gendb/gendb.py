# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue
import threading, time

import requests
import sqlite3

PROCESS_MAX = 16
QUEUE_MAX = 200
retry_count = 5

ON = True
proxy == None

def unit_getpage(url_queue, page_queue):
	'''从url队列拉取->用代理请求页面内容->放入页面队列'''
	# Process(target=, args=()).start() < PROCESS_MAX
	while ON:
		if url_queue.empty():
			time.sleep(1)
			print("[waiting] <url> queue is empty")
		else:
			url = url_queue.get()
			if proxy == None:
				proxy = requests.get("http://123.207.35.36:5010/get/").content
			while 1:
				try:
					html = requests.get(url, proxies={"http": "http://%s"%proxy}).content
					page_queue.put((html, url))
					break
				except Exception:
					if retry_count > 0:
						proxy = None
						break
					retry_count -= 1

def unit_parser(page_queue, url_queue, data_queue):
	'''拉取页面队列->分选项解析页面->写回数据/url队列'''
	while ON:
		if page_queue.empty():
			time.sleep(1)
			print("[waiting] <page> queue is empty")
		else:
			page_with_url = page_queue.get()
			runparser(page_with_url, url_queue, data_queue)

def unit_writedb(data_queue):
	'''拉取数据->序列化/写数据库'''
	while ON:
		if data_queue.empty():
			time.sleep(1)
			print("[waiting] <data> queue is empty")
		else:
			data = data_queue.get()
			print("sql_mode")

if __name__ == '__main__':
	url_queue = Queue()
	page_queue = Queue()
	data_queue = Queue()

	url_queue.put("https://bgm.tv/")
	
	for i in range(0, PROCESS_MAX):
		Process(target=unit_getpage, args=(url_queue, page_queue)).start()
	threading.Thread(target=unit_parser, args=(page_queue, url_queue, data_queue)).start()
	threading.Thread(target=unit_writedb, args=(data_queue)).start()
	