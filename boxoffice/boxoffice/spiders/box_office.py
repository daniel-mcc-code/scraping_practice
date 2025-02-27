import scrapy


class BoxOfficeSpider(scrapy.Spider):
    name = "box_office"
    allowed_domains = ["boxofficemojo.com"]
    
    years = list(range(2010, 2026))

    start_urls = [f"https://www.boxofficemojo.com/year/world/{str(year)}" for year in years]
    

    def parse(self, response):
            yield {
                "url": response.url,
                "ranks": response.css("td:nth-child(1)::text").getall(),
                "film_titles": response.css("td > a::text").getall(),
                "film_links": response.css("td > a::attr(href)").getall(),
                "worldwide_gross": response.css("td:nth-child(3)::text").getall(),
                "domestic_gross": response.css("td:nth-child(4)::text").getall(),
                "foreign_gross": response.css("td:nth-child(6)::text").getall()

            }
        


class BoxOffice2Spider(scrapy.Spider):
    name = "box_office2"
    allowed_domains = ["boxofficemojo.com"]
    
    start_urls = ["https://www.boxofficemojo.com/year/world/2010"]

    def start_requests(self):
          for url in self.start_urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
          response.css("li.a-dropdown_item > a::attr(data-value)").getall()
    

    def parse_movie_data(self, response):
            yield {
                "url": response.url,
                "ranks": response.css("td:nth-child(1)::text").getall(),
                "film_titles": response.css("td > a::text").getall(),
                "film_links": response.css("td > a::attr(href)").getall(),
                "worldwide_gross": response.css("td:nth-child(3)::text").getall(),
                "domestic_gross": response.css("td:nth-child(4)::text").getall(),
                "foreign_gross": response.css("td:nth-child(6)::text").getall()

            }
        
