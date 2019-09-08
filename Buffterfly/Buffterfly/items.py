# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BuffterflyItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()


class TopicItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    avatar = scrapy.Field()


class DetailItem(scrapy.Item):
    url = scrapy.Field()
    images = scrapy.Field()
