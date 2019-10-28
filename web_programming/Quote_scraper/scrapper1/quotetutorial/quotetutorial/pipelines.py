# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class QuotetutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=sqlite3.connect("myquotes.db")
        self.curr=self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                         title text,
                         author text
                         )""")

    def process_item(self, item, spider):
        self.curr.execute("""insert into quotes_tb values(?,?)""",(
                item['title'][0],
                item['author'][0]
        ))
        self.conn.commit()
        return item
