# -*- coding:utf-8 -*-
import scrapy
import os
import sys
import json
import time

#https://github.com/shiyanlou?tab=repositories
#"name": "trojan",
#"update_time": "2017-06-20T11:10:55Z"

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        url_tmpl='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        print('******************************************************')
        for github_name in response.xpath('//li[contains(@class,"public") and contains(@class,"source")]'):
            namelib = github_name.xpath('.//div[contains(@class,"d-inline-block") and contains(@class, "mb-1")]/h3/a/text()').extract()
            name1 = namelib[0].replace(' ','')
            name2 = name1.replace('\n','')

            datalib = github_name.xpath('.//div[contains(@class,"f6") and contains(@class, "text-gray")]/relative-time/@datetime').extract()
            lib = {'name':name2, 'update_time':datalib[0]}

#            with open('F:\python编写\实验楼\\2048\scrapy_learn\shiyanlougithub.json','a') as f:
#                f.write(json.dumps(lib) + '\n')
            print(lib)

    #        for i in
#            print(github_name.xpath('//relative-time').extract())
