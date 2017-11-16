# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import json

logger = logging.getLogger(__name__)


class TencentpositionPipeline(object):
    def process_item(self, item, spider):
        logger.info(item)

        with open('./tencent_positions.txt','a') as f:
            f.write(json.dumps(item,ensure_ascii=False,indent=2))

        return item
