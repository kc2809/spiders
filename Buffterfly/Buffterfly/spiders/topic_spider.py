import scrapy
import logging
from ..items import BuffterflyItem
from ..items import TopicItem
import json
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
import datetime

class PicthTopicSpider(scrapy.Spider):
    name = "topic"

    def start_requests(self):
        urls = ["http://www.pic-th.com/ajax/load.php?action=load_all&page=1"]
        for url in urls:
            yield SplashRequest(url, self.parse, args={"wait": 2})

    def parse(self, response):
        self.logger.info(datetime.datetime.now())
        topics = self.getTopicItemFromResponse(response)
        for item in topics:
            yield item

    def getTopicItemFromResponse(self, response):
        htmlSource = self.getHtmlFromResponse(response.body)
        topics = self.parseTopicItem(htmlSource)
        if not topics:
            self.logger.error("Could not parse html source structure has changed")
        return topics

    def getHtmlFromResponse(self, jsonString):
        try:
            data = json.loads(jsonString)
            return data["html"]
        except (ValueError):
            return ""

    def parseTopicItem(self, htmlSource):
        topics = []
        if not htmlSource:
            self.logger.error(
                "Empty Source http://www.pic-th.com/ajax/load.php?action=load_all&page=1 structure has changed"
            )
            return topics
        x = Selector(text=htmlSource).xpath("//a").getall()
        for diva in x:
            ablock = Selector(text=diva)
            topicItem = TopicItem()
            topicItem["name"] = ablock.xpath("//a/@href").get()
            topicItem["src"] = ablock.xpath("//img/@src").get()
            topicItem["topicUrl"] = ablock.xpath("//p/text()").get()
            topics.append(topicItem)

        return topics
