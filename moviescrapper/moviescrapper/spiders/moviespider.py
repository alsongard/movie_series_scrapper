import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["yts.mx"]
    start_urls = ["https://yts.mx/"]

    def parse(self, response):
        pass
