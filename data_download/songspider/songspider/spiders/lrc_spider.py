from scrapy import Spider
from ..items import SongspiderItem


class LrcSpider(Spider):
    name = 'lrcspider'
    start_urls = [
        "http://so.gushiwen.org/type.aspx?p=1"
    ]

    def parse(self, response):
        poetry = SongspiderItem()
        poetry['poetry_name'] = "wenchao...."
        poetry['author_name'] = "author name test"
        poetry['author_decade'] = "Tang"
        yield poetry
