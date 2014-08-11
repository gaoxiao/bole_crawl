# coding=utf-8

'''
Created on 2014-8-11

@author: gaoxiao.gx
'''

import MySQLdb

if __name__ == '__main__':
    for i in xrange(1, 3):
        db = MySQLdb.connect("localhost", "root", "root", "bole", charset='utf8')
        cursor = db.cursor()
        sql = '''
        insert into info_info 
        (title, content, view_times, info_area_id, info_class_id, pub_date) 
        VALUES 
        ('噶松岛枫是', 'asd', 0, 1, 2, '2014-08-06 03:21:07')
        '''
        cursor.execute(sql)
        db.commit()
