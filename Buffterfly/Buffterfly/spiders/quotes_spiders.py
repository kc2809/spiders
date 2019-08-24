import scrapy
import logging
from ..items import BuffterflyItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        self.logger.info('START CRAWALER ')
        print('START CRAWALER')
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        for quote in response.css('div.quote'):
            bu = BuffterflyItem()
            bu['name'] = quote.css('span.text::text').get()
            bu['price'] = quote.css('small.author::text').get()
            yield bu