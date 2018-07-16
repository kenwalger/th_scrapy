from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class HorseSpider(CrawlSpider):
    name = 'horses'
    allowed_domains = ['http://www.horsechannel.com']
    url_start = ['http://www.horsechannel.com']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse',
                  follow=True)]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is {}'.format(title))
