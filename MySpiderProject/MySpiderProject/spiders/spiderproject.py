# -*- coding: utf-8 -*-
import scrapy


class SpiderprojectSpider(scrapy.Spider):
    name = 'spiderproject'   #爬虫文件的名称，爬虫源文件的唯一标识
    #allowed_domains = ['www.xxx.com']  #允许的域名，一般不用，用了会限定url列表里面的元素
    start_urls = ['https://www.baidu.com/']  #起始的url列表，列表中的元素会被scrapy自动的进行请求发送

    def parse(self, response):
        pass
