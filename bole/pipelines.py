# coding=utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import datetime
import re

class BolePipeline(object):
	filename = 'bole.txt'

	def __init__(self):
		self.f = open(self.filename, 'w+')
		self.db = MySQLdb.connect("localhost", "root", "root", "bole", charset='utf8')
	
	def process_item(self, item, spider):

# 		self.f.write("%s##" % (item['title'][0].encode('GBK')))
# 		self.f.write("%s##" % (item['info_class'][0].encode('GBK')))
# 		self.f.write("%s##" % (item['info_area'][0].encode('GBK')))
# 		self.f.write("%s##" % (item['pub_date'][0].encode('GBK')))
# 		self.f.write("%s" % (item['content'][0].encode('GBK')))

		# 处理时间
		pub_date = item['pub_date'][0]
		pub_date = pub_date.strip()[-10:]
		
		content = ""
		for l in item['content']:
			l = l.strip()
			if l :
				content += l
 		
 		cursor = self.db.cursor()
 		
 		sql = """
 		insert into info_info 
 		(title, content, view_times, info_area_id, info_class_id, pub_date) 
 		VALUES ('%s', '%s', 0, '%s', '%s', '%s')
 		""" 
 		sql = sql % (item['title'][0].encode('utf-8'),
					content.encode('utf-8'), '1' , '2',
					pub_date.encode('utf-8'))
 		
 		cursor.execute(sql)
		self.db.commit()
 		
		return item
	
	def __del__(self):
		self.db.close()
