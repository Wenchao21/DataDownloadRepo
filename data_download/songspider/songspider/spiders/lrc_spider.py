#coding=utf-8
from scrapy import Spider
from ..items import SongspiderItem


class LrcSpider(Spider):
    name = 'lrcspider'
    start_urls = [
        "http://so.gushiwen.org/type.aspx?p=1"
    ]

    def parse(self, response):
        poetry = SongspiderItem()
        poetry['poetry_name'] = u"wenchao...李白"
        poetry['poetry_comments'] = str(response.selector.xpath('//span/text()').extract()).encode('UTF-8')
        poetry['author_name'] = response
        poetry['author_decade'] = "Tang"
        yield poetry
