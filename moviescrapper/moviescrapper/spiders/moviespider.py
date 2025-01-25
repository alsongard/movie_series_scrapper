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
                'movie_release_year' : movie.css("div.browse-movie-bottom div::text").get()
            }