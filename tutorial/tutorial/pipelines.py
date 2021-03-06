# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import os

con = None


class SQLitePipeline(object):

    def __init__(self):
        self.setup_db()
        # self.create_table()

    def setup_db(self):
        self.con = sqlite3.connect(os.getcwd() + '/test.db')
        self.cur = self.con.cursor()

    # def create_tables(self):
    #     self.dropAmazonTable()
    #     self.createAmazonTable()

    # def create_table(self):
    #     self.cur.execute("CREATE TABLE E_bate ("
    #                      "title varchar(512), "
    #                      "keywords varchar(512), "
    #                      "description varchar(512),"
    #                      "url varchar(512))")

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        values = (
            str(item['title']),
            str(item['keywords']),
            str(item['description']),
            str(item['url'])
        )

        sql = 'INSERT INTO E_bate VALUES(?,?,?,?)'

        self.cur.execute(sql, values)
        self.con.commit()

    def close_db(self):
        self.con.close()
