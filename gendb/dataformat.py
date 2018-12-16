# coding:utf-8

anime_base = {
	"name" : {"zh":"", "jp":"", "nhg":"", "en":""} , # 名字 中文 日语 罗马音 英语
	"cover" : None , # 封面(base64/blob/url)
	"time" : [2000,10], # 放送开始(yy/mm)
	"episodes" : 13, # 话数
	"staff" : {}, # staff
	"baseinfos" : {}, # 一些基本信息
	"story" : "", # 故事简介
	"tags" : #标签
	{
		"genre" : [], # 类型
		"label" : {}, # bgmtv的标注数据
	},
	"ranking" : {}, # 评分
	"cast" : {}, # 角色
	"relate" : # 相关
	{
		"bgm" : [], # 音乐
		"series" : [], # 系列
		"recommend" : [], # 相关推荐
	},
	"origin" : {}, # 引用来源请注名
}

chara_base = {
	"name" : {"zh":"", "jp":"", "nhg":"", "en":""} , # 名字 中文 日语 罗马音 英语
	"sex" : 0 , # 妹子0/汉子1
	"picture" : None , # 截图(base64/blob/url)
	"tags" : #标签
	{
		"cv" : "", # 声优
		"label" : [], # 给角色打标签
	},
	"relate" : #相关
	{
		"acted" : [], # 出演
		"similar" : [], # 类似角色
	},
	"origin" : {}, # 引用来源请注名
}