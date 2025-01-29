# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class MoviescrapperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_rating = scrapy.Field()
    movie_url = scrapy.Field()
    movie_release_year = scrapy.Field()
    movie_category = scrapy.Field()