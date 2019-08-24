import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
# from Buffterfly.Buffterfly.spiders.quotes_spiders import QuotesSpider
from Buffterfly.Buffterfly.spiders.topic_spider import PicthTopicSpider

import logging
from scrapy.utils.log import configure_logging

settings = get_project_settings()

runner = CrawlerRunner(settings)


configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)


@defer.inlineCallbacks
def crawl():
    # yield runner.crawl(QuotesSpider)
    yield runner.crawl(PicthTopicSpider)
    reactor.stop()

crawl()
reactor.run()