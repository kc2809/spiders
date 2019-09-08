import scrapy
import logging
from ..items import DetailItem
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from ..helpers.mongo_helper import DBHelper

import datetime


class DetailSpider(scrapy.Spider):
    name = "detail"
    TOPIC_DETAIL_URL = 'http://www.pic-th.com/topic-$topicId.html'

    def start_requests(self):
        urls = self.generateUrls()
        for url in urls:
            yield SplashRequest(url, self.parse, args={"wait": 2})

    def generateUrls(self):
        urls = []
        currentSize = DBHelper.getCurrentTopicSize()
        maxSize = DBHelper.getMaxSizeTopic()
        [urls.append(self.TOPIC_DETAIL_URL.replace("$topicId", str(i)))
         for i in range(currentSize, maxSize)]
        return urls

    def parse(self, response):
        print(response._url)
        self.logger.info(datetime.datetime.now())
        detailItem = DetailItem()
        self.parseDetailItem(detailItem, response)
        yield detailItem

    def parseDetailItem(self, detailItem, response):
        detailItem['url'] = self.parseUrl(response)
        detailItem['images'] = self.parseImages(response.body)

    def parseUrl(self, response):
        realUrlArr = response._url.split('/')
        return realUrlArr[-1]

    def parseImages(self, body):
        return Selector(text=body).xpath('//div[@id="content"]/img/@src').getall()
