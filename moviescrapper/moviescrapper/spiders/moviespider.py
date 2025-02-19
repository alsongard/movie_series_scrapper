import scrapy
import os
import pandas as pd
from moviescrapper.items import MovieItem
class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["yts.mx"]
    start_urls = ["https://yts.mx/browse-movies"]
    page_count = 0
    max_count = 30

    def parse(self, response):
        # get all movies
        movies = response.css("div.browse-movie-wrap")
            
        for movie in movies:
            movie_item = MovieItem()
            movie_item["movie_name"] = movie.css("div.browse-movie-bottom  a::text").get()
            movie_item["movie_rating"] = movie.css("h4.rating::text").get()
            movie_item["movie_url"] = movie.css("div.browse-movie-bottom a::attr(href)").get()
            movie_item["movie_release_year"] = movie.css("div.browse-movie-bottom div::text").get()
            movie_item["movie_category"] = movie.xpath("//figcaption/h4[not(@class='rating')]/text()").get()
            
            yield movie_item
        
        self.page_count += 1
        self.log(f"Scraped  {self.page_count} pages")

        if self.page_count == self.max_count:
            self.log("Reached maximum and now exiting")
            return

        next_page = response.xpath("//section/following-sibling::*[1]/ul/li[11]/a/@href").get()
        if next_page is None:
            next_page = response.xpath("//section/following-sibling::*[1]/ul/li[12]/a/@href").get()

        
            
        if next_page:
            next_page_url = response.urljoin(next_page)
            self.log(f"Print next page : {next_page_url}")
            yield response.follow(next_page_url, callback=self.parse) 
        

        
        # self.append_to_csv(new_data)
        # increase the page count 


        # for movie in movies:
        #     yield{
        #         'movie_name': response.css("div.browse-movie-bottom  a::text").get(),
        #         'movie_rating': response.css("h4.rating::text").get(),
        #         'movie_url' : response.css("div.browse-movie-bottom a::attr(href)").get(),
        #         'movie_release_year' : response.css("div.browse-movie-bottom div::text").get(),
        #         'movie_category' : response.xpath("//figcaption/h4[not(@class='rating')]/text()").get() #or you could use following sibliing
        #     }
            

        



    # def append_to_csv(self, new_data):
    #     """Appends new data to CSV, avoiding duplicates"""
    #     df_new = pd.DataFrame(new_data)

    #     if os.path.exists(self.csv_file):
    #         print("the path exist and we read data fron the given file")
    #         data_existing_df =  pd.read_csv(self.csv_file)
    #         data_combined_df = pd.concat([data_existing_df, df_new]).drop_duplicates(subset=["movie_name"], keep="first")
    #     else:
    #         data_combined_df = df_new
        
    #     data_combined_df.to_csv("new_movie_data.csv", index=False)
    #     self.log(f"Saved {len(data_combined_df)} to total  unique movies to  {self.csv_file}")


        # movie_item = MovieItem()



# /browse-movies?page=4
#  https://yts.mx/browse-movies?page=4