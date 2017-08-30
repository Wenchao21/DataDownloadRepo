from scrapy import Spider
from ..items import SongspiderItem


class LrcSpider(Spider):
    name = 'lrcspider'
    allowed_domains = ["gushici.org"]
    start_url = [
        "http://so.gushiwen.org/type.aspx?p=1"
    ]

    def parse(self, response):
        item1 = SongspiderItem()
        item1['name'] = "wenchao...."
        yield item
