'''
完整的一个静态番站结构

挂载点:
	/index.html => /
		GET /json/tag/index.json
	/tag/搞笑/index.html => /tag/搞笑
		GET /json/tag/搞笑.json
	/info/神样家族/index.html => /info/神样家族
		GET /json/info/神样家族.json
	/info/小清水亚美/index.html => /info/小清水亚美
		GET /json/info/小清水亚美.json
静态:
	/404.html
	/static/bootstrap/js
	/static/bootstrap/css
	/static/picture/神样家族.png|jpg
数据库:
	/json/info/神样家族.json
	/json/tag/搞笑.json
'''
