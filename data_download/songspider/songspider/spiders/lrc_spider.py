
from scrapy import Spider
from ..items import SongspiderItem
class LrcSpider(Spider):
    name = 'lrcspider'
    start_url = [
        "www.baidu.com"
    ]

    def parse(self, response):
        item1 = SongspiderItem()
        item1['name'] = "wenchao...."
        yield item
