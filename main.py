import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from Buffterfly.Buffterfly.spiders.quotes_spiders import QuotesSpider
from Buffterfly.Buffterfly.spiders.topic_spider import PicthTopicSpider
from Buffterfly.Buffterfly.spiders.detail_spider import DetailSpider

import logging
from scrapy.utils.log import configure_logging
import os
# Must be at the top before other imports
os.environ.setdefault('SCRAPY_SETTINGS_MODULE',
                      'Buffterfly.Buffterfly.settings')

# number  page will be load
PAGE_NUMBER = 100

SPLASH_URL = 'http://192.168.1.219:8050'

settings = get_project_settings()
settings.set('PAGE_NUMBER', PAGE_NUMBER)
settings.set('SPLASH_URL', SPLASH_URL)

runner = CrawlerRunner(settings)

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(PicthTopicSpider)
    yield runner.crawl(DetailSpider)
    reactor.stop()


crawl()
reactor.run()
