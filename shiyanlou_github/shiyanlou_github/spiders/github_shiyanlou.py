# -*- coding:utf-8 -*-
import scrapy
from shiyanlou_github.items import ShiyanlouGithubItem

class ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlou_github'
    allowed_domains = ['https://github.com/shiyanlou?tab=repositories']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for github in response.css('li.public'):
            item = ShiyanlouGithubItem({
            'name':github.xpath('.//div[contains(@class,"d-inline-block")]/h3/a/text()').re_first('\s*(.+)'),
            'update_time':github.xpath('.//div[contains(@class, "text-gray")]/relative-time/@datetime').extract_first()
            })
            yield item
