#!/usr/bin/env python
# encoding: utf-8

from scrapy.spiders import Spider
import re

class SgyySpider(Spider):
    name = 'Sgyy_spider'
    start_urls = ['http://www.purepen.com/sgyy/index.htm']

    def parse(self, response):
        urls = re.search("\d+.htm", str(response),flags=0)
#        for i in urls:
#            print type(i)

