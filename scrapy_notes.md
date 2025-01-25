- create environment
python3 -m venv directoryname

- activate environment
source/bin/activate

- pip install scrapy
python3 -m pip install scrapy

- install scrapy
scrapy startproject moviewscrapper

by default, you will have no spider.py file in spiders folder


- how to create a scrapy spider
- using scrapyy shell to find our CSS selectors
- Using CSS Selectors in our spider to get data
- Getting our spider to navigate to Multiple Pages


- to generate moviescrapper
```
scrapy genspider moviescrapper https://yts.mx/
```
Syntax: 
``scrapy genspider moviescrapper siteName``

Go to settings and change starturl to : ``https://yts.mx/trending-movies``

### **Getting started with scrapy shell
``pip install ipython``

Go to scrapy.cfg
Add following:
``shell=ipython``

in terminal :
```
scrapy shell
fetch("https://yts.mx/browse-movies")
# response.css("div.className") to get the movie container
movies = response.css("div.browse-movie-wrap")


# get htlm output on terminal
response.css("div.browse-movie-wrap").get()


len(movies) # returns 20
```

## get movie data on the following
When you want to get the href(link) from an anchor tag element, use the ``attr(href)``

movie name : element : div class:browse-movie-bottom | element: a::text
``canada_movie.css("div.browse-movie-bottom  a::text").get()`` # returns the name of the movie

rating : element : h4 class rating
``canada_movie.css("h4.rating::text").get()`` # returns the rating of the movie

year release: div browse-movie-year
``canada_movie.css("div.browse-movie-bottom div::text").get()`` # returns year of release of movie


link for more information on movie: element:  div class browse-movie-wrap | element :a browse-movie-link  href
``canada_movie.css("div.browse-movie-title a::attr(href)").get()``


