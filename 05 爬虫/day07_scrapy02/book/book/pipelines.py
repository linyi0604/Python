# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from book.settings import MONGO_HOST,MONGO_PORT,DB,COLLECTION
class BookPipeline(object):
    # spider 开始执行的时候会执行一次这个函数
    def open_spider(self,spider):
        self.con = MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        self.collection = self.con[DB][COLLECTION]

    # spider 结束时候会执行一次
    def close_spider(self,spider):
        self.con.close()

    def process_item(self, item, spider):
        self.collection.save(dict(item))
        return item
