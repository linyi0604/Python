# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import json
logger = logging.getLogger('传智老师')


'''
在这里存储数据,  每个pipline都会被调用,根据注册的权重 调用顺序不同
'''

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        print('到达pip')
        logger.info(item)

        return item


class MyspiderPipeline1(object):
    def process_item(self, item, spider):
        print( '到达pip1! ')
        with open('./itcast_teachers.txt' , 'a' ) as f:
            f.write( json.dumps(item,ensure_ascii=False,indent=2) )
        return item