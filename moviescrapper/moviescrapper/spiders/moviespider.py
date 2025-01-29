import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["yts.mx"]
    start_urls = ["https://yts.mx/browse-movies"]

    def parse(self, response):
        # get all movies
        movies = response.css("div.browse-movie-wrap")

        for movie in movies:
            yield{
                'movie_name': movie.css("div.browse-movie-bottom  a::text").get(),
                'movie_rating': movie.css("h4.rating::text").get(),
                'movie_url' : movie.css("div.browse-movie-bottom a::attr(href)").get(),
                'movie_release_year' : movie.css("div.browse-movie-bottom div::text").get(),
                'movie_category' : movie.xpath("//figcaption/h4[not(@class='rating')]/text()").get() #or you could use following sibliing
            }

        next_page = response.xpath("//section/following-sibling::*[1]/ul/li[11]/a/@href").get()
        if next_page is None:
            next_page = response.xpath("//section/following-sibling::*[1]/ul/li[12]/a/@href").get()

            
        if next_page:
            next_page_url = response.urljoin(next_page)
            self.log(f"Print next page : {next_page_url}")
            yield response.follow(next_page_url, callback=self.parse) 




# /browse-movies?page=4
#  https://yts.mx/browse-movies?page=4