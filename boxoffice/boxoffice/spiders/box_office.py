import scrapy


class BoxOfficeSpider(scrapy.Spider):
    name = "box_office"
    allowed_domains = ["boxofficemojo.com"]
    start_urls = ["https://boxofficemojo.com"]

    def parse(self, response):
        pass
