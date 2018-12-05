# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.utils.project import get_project_settings
import pymysql
# case案例
class ZbjPipeline1(object):
    def open_spider(self, spider):
        # setting就是一个字典，字典的键值就是所有的配置选项
        # settings = get_project_settings()
        # 链接数据库
        # self.db = pymysql.Connect(host=settings['HOST'], port=settings['PORT'], user=settings['USER'], password=settings['PWD'], database=settings['DB'], charset=settings['CHARSET'])
        self.db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='zbj',charset='utf8')

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        self.save_to_mysql(item)
        return item

    def save_to_mysql(self, item):
        # 获取cursor
        cursor = self.db.cursor()
        # 拼接sql语句,values ('{}',{},'{}','{}','{}','{}')
        sql = 'insert into works (case_name, case_img, case_link, case_price, company_id)values ("?","?","?","?","?")'
        param = (item["case_name"], item["case_img"], item["case_link"], item["case_price"], item["company_id"])

        # sql = """insert into case (case_name, case_img, case_link, case_price, company_id) values("%s","%s","%s","%s","%s") """%(item["case_name"], item['case_img'], item['case_link'], item['case_price'], item['company_id'])
        # 执行sql语句
        try:
            cursor.execute(sql,param)
            self.db.commit()
        except Exception as e:
            print('*'*50)
            print(e)
            self.db.rollback()
# comment评论
class ZbjPipeline(object):
    def open_spider(self, spider):
        # 链接数据库
        self.db = pymysql.connect(host='10.8.157.39',port=3306,user='root',password='123456',database='zbj',charset='utf8')

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        self.save_to_mysql(item)
        return item

    def save_to_mysql(self, item):
        # 获取cursor
        cursor = self.db.cursor()
        # 拼接sql语句,values ('{}',{},'{}','{}','{}','{}')
        sql = 'insert into comments (user_name, user_case, price, company_id, impression,content,comment_time)values ("{}","{}","{}","{}","{}","{}","{}")'
        sql = sql.format(item["user_name"], item["user_case"], item["price"], item["company_id"], item["impression"],item["content"],item["comment_time"])

        # 执行sql语句
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print('*'*50)
            print(e)
            self.db.rollback()

import sqlite3
class SqlitePipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('test')
        self.cur = self.conn.cursor()
    def close_spider(self,spider):
        self.conn.close()
    def process_item(self,item,spider):
        sql1 = "insert into mycase(case_name, case_img, case_link, case_price,company_id) values ('{}','{}','{}','{}','{}')"
        sql = sql1.format(item["case_name"], item['case_img'], item['case_link'], item['case_price'], item['company_id'])
        # sql = """insert into case (case_name, case_img, case_link, case_price, company_id) values("%s","%s","%s","%s","%s") """ % (
        # item["case_name"], item['case_img'], item['case_link'], item['case_price'], item['company_id'])
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
