#!/bin/bash
cd /home/alson-kali/PROGRAMMING/movie_series_scrapper
source bin/activate
cd moviescrapper/data/

path=/home/alson-kali/PROGRAMMING/movie_series_scrapper/moviescrapper/data
# this echos the entire path(absolute) for each file
for entry in "$path"/*
do
    echo $entry
done

working_directory=`pwd`
echo "Working directory is ${working_directory}"

#  will be using listing solution
myfiles=`ls *.csv`
for eachFile in $myfiles
do
    if [[ $eachFile == "new_movies_data.csv" ]]; then
        rm $eachFile
    fi

done

echo "scrapy crawl moviespider -o new_movies_data.csv"
scrapy crawl moviespider -o new_movies_data.csv

# git add . 
# git commit -m "new movie data added"
# git push 