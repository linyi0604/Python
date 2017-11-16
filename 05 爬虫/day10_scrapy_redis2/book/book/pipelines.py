# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class BookPipeline(object):
    def process_item(self, item, spider):
        item["book_cate"] = self.process_book_cate(item["book_cate"])
        item["book_name"] =item["book_name"].split("》")[0].split("《")[-1]
        print(item)
        return item

    def process_book_cate(self,book_cate):
        book_cate = [i.strip() for i in book_cate if len(i.strip())>0 and i.strip()!="›"]
        return book_cate

