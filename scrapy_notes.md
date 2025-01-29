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


link for more information on movie: element:  div class browse-movie-bottom | element : anchor 
`` canada_movie.css("div.browse-movie-bottom a::attr(href)").get()``


In moviespider.py add the following in the  parse() function
```
def parse(self, response):
    movies = response.css("div.browse-movie-wrap")

    for movie in movies:
        yield{
            'movie_name': movie.css("div.browse-movie-bottom  a::text").get(),
            'movie_rating': movie.css("h4.rating::text").get(),
            'movie_url' : movie.css("div.browse-movie-bottom a::attr(href)").get(),
            'movie_release_year' : movie.css("div.browse-movie-bottom div::text").get()
        }
```

## getting multiple pages
```
response.xpath("//section/following-sibling::*[1]/ul/li[11]/a/@href").get() # returns /browse-movies?page=2'

# in moviespider.py add

next_page = response.xpath("//section/following-sibling::*[1]/ul/li[11]/a/@href").get()
if next_page is not None:
    next_page_url = 'https://yts.mx' + next_page
    yield response.follow(next_page_url, callback=self.parse)
```


https://yts.mx/browse-movies/browse-movies?page=2 // this does not work
https://yts.mx/browse-movies?page=2 // this works click to 


yts.mx has a total of yts.mx 3247 pages where by each page has 20 movies excepts of the last which has 17  movies
Calculate total movies:
```
echo $((3246 * 20)) = 64920
echo $((64920 + 17))
https://yts.mx/movies/aloft-2014
```


To exclude a given class:
One must specify the data he/she wants without text() it returns the html element. This is different with how css() selector works, in that you pass the .get() and returns the data
```
response.xpath("//figcaption/h4[not(@class='rating')]/text()").get()
```


## having different links to the nextpage:
First:
Instead of concatenating the web url together with the next_page link use the method : 
``response.urljoin()``
pass in the next_page link.

**handling the different links**
by default:

```
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
        next_page_url = response.joinurl(next_page)
        self.log(f"Print next page : {next_page_url}")
        yield response.follow(next_page_url, callback=self.parse) 
```