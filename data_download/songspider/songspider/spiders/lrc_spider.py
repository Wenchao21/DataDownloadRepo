from scrapy import Spider
from ..items import SongspiderItem


class LrcSpider(Spider):
    name = 'lrcspider'
    start_urls = [
        "http://so.gushiwen.org/type.aspx?p=1"
    ]

    def parse(self, response):
        poetry_name_data = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]//b')
        poetry_author_name = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]//p[@class="source"]//a[2]')
        poetry_author_decade = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]//p[@class="source"]//a[1]')
        poetry_comments_data = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]/div[@class="contson"]')
        au = poetry_author_name.xpath('string(.)').extract()
        pn = poetry_name_data.xpath('string(.)').extract()
        pad = poetry_author_decade.xpath('string(.)').extract()
        pcd = poetry_comments_data.xpath('string(.)').extract()
        for i in range(0, len(pn)):
            poetry = SongspiderItem()
            poetry['poetry_name'] = pn[i]
            poetry['author_name'] = au[i]
            poetry['author_decade'] = pad[i]
            poetry['poetry_comments'] = pcd[i]
            yield poetry
