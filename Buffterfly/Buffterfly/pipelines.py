# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import TopicItem
from .helpers.mongo_helper import DBHelper

import re


class BuffterflyPipeline(object):
    max = 0

    def open_spider(self, spider):
        print('OPEN SPIDER')

    def close_spider(self, spider):
        print('CLOSE SPIDER')
        print(self.max)
        DBHelper.insertMaxSizeTopic(self.max)

    def process_item(self, item, spider):
        if isinstance(item, TopicItem):
            self.processTopicItem(item)
        return item

    def processTopicItem(self, item):
        print(item)
        DBHelper.insertTopic(item)
        self.calculateMaxSizeTopic(item)

    def calculateMaxSizeTopic(self, item):
        self.max = max(self.max, self.getTopicId(item))

    def getTopicId(self, item):
        return int(re.findall('\d+', item['url'])[0])
