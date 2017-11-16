# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re


class CsdnPipeline(object):
    def process_item(self, item, spider):
        item['article_title'] = self.handle_article_title(item['article_title'])
        # print(item)

        return item


    def handle_article_title(self,title):
        title = [ re.sub(r'\r\n','',i) for i in title ]
        title = [re.sub(r'\s+', '', i) for i in title]
        title = [ i for i in title if len(i)>0 ]
        title = ' '.join(title)
        return title