# coding=utf8

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from bole.items import BoleItem

class CarcrawlerSpider(CrawlSpider):
    name = 'boleCrawler'
    allowed_domains = ['lovebanker.com']
    start_urls = ['http://www.lovebanker.com/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'bank/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        hxs = HtmlXPathSelector(response)
        i = BoleItem()
        i['title'] = hxs.xpath('//div[@class="article"]/h2/text()').extract()
        i['info_class'] = hxs.xpath('//div[@class="article_info"]/div[@class="textl"]/a[2]/text()').extract()
        i['info_area'] = hxs.xpath('//div[@class="article_info"]/div[@class="textl"]/a[3]/text()').extract()
        i['pub_date'] = hxs.xpath('//div[@class="article_info"]/div[@class="textr"]/text()').extract()
        
        i['content'] = hxs.xpath('//div[@class="article"]/div[@class="context"]/p').extract()
        return i
