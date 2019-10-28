import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

      items=QuotetutorialItem()

      all_div_quotes=response.css("div.quote")

      for quotes in all_div_quotes:
        title = quotes.css("span.text::text").extract()
        author = quotes.css(".author::text").extract()

        items['title']=title
        items['author']= author

        yield items

      next_page=response.css('li.next a::attr(href)').get()

      if next_page is not None:
          yield response.follow(next_page,callback=self.parse)
