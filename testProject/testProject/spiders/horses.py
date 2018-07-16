import scrapy


class HorseSpider(scrapy.Spider):
    name = 'horse'

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/']

        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        page = url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        print('URL is: {}'.format(url))
        with open(filename, 'wb') as file:
            file.write(response.body)
        print('Saved file %s' % filename)

