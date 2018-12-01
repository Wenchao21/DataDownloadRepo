#coding=utf-8
from scrapy import Spider
from ..items import SongspiderItem
from scrapy import Request


class LrcSpider(Spider):
    name = 'lrcspider'
    start_urls = [
        "http://so.gushiwen.org/type.aspx?p=1"
    ]

    def parse(self, response):
        baseurl = "http://so.gushiwen.org"
        poetry_name_data = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]//b')
        poetry_author_name = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]//p[@class="source"]//a[2]')
        poetry_author_decade = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]//p[@class="source"]//a[1]')
        poetry_comments_data = response.xpath('//div[@class="left"]//div[@class="sons"]//div[@class="cont"]/div[@class="contson"]')
        pages_data = response.xpath('//div[@class="left"]//div[@class="pages"]//a[last()]/@href').extract()
        pages_data_comment = response.xpath('//div[@class="left"]//div[@class="pages"]//a[last()]')

        pd = pages_data_comment.xpath('string(.)').extract()
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

        if pd and pd[0] == "下一页":
            url = baseurl + pages_data[0]
            yield Request(url, callback=self.parse)
