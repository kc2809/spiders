import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from Buffterfly.Buffterfly.spiders.quotes_spiders import QuotesSpider
from Buffterfly.Buffterfly.spiders.topic_spider import PicthTopicSpider

import logging
from scrapy.utils.log import configure_logging

# number  page will be load
PAGE_NUMBER = 10

settings = get_project_settings()
settings.set('ITEM_PIPELINES', {
    'Buffterfly.Buffterfly.pipelines.BuffterflyPipeline': 300,
})

settings.set('PAGE_NUMBER', PAGE_NUMBER)
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
