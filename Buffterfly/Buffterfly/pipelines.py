# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import TopicItem
from .items import DetailItem
from .helpers.mongo_helper import DBHelper

import re


class BuffterflyPipeline(object):
    max = 0

    def open_spider(self, spider):
        print('OPEN SPIDER ' + spider.name)
        self.max = 0

    def close_spider(self, spider):
        print('CLOSE SPIDER ' + spider.name)
        self.closeDetailSpider(spider)
        self.closeTopicSpider(spider)
        print(self.max)

    def closeDetailSpider(self, spider):
        if(spider.name == 'detail'):
            DBHelper.updateCurrentSizeByAddingLoadedTopic(self.max)

    def closeTopicSpider(self, spider):
        if(spider.name == 'topic'):
            DBHelper.insertMaxSizeTopic(self.max)
            if DBHelper.getCurrentTopicSize() == 0:
                DBHelper.updateCurrentSize(0)

    def process_item(self, item, spider):
        if isinstance(item, TopicItem):
            self.processTopicItem(item)
        if isinstance(item, DetailItem):
            self.processDetailItem(item)
        print(item)
        return item

    def processDetailItem(self, item):
        self.max += 1
        DBHelper.insertImagesToTopic(item)

    def processTopicItem(self, item):
        DBHelper.insertTopic(item)
        self.calculateMaxSizeTopic(item)

    def calculateMaxSizeTopic(self, item):
        self.max = max(self.max, self.getTopicId(item))

    def getTopicId(self, item):
        return int(re.findall('\d+', item['url'])[0])
