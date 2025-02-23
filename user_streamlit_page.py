import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.logo(
    image="https://yts.mx/assets/images/website/logo-YTS.svg",
    size="large"
)
st.sidebar.write("YTS.MX scrapper analyzer")
user_options = ["year", "category"]
entered_option = st.sidebar.selectbox("Select movie based on :", user_options)
st.write("### YTS.MX MOVIES")

# ultimatum file which i added movies for first scrapy and second scrapy
data_df = pd.read_csv("./moviescrapper/data/all_movie_data.csv")

# st.write("data_df from /moviescrapper/data/all_movie_data.csv")
data_df.drop(data_df.columns[data_df.columns.str.contains('Unnamed')], axis=1, inplace=True) # drop Unnamed column
# data_df

# get data from new file:
# get_new_data_daily_df = pd.read_csv("./moviescrapper/data/new_movies_data.csv")
get_new_data_daily_df = pd.read_csv("./moviescrapper/data/new_movies_data.csv")

# st.write("Getting data from /moviescrapper/data/all_movie_data.csv")
get_new_data_daily_df.drop(get_new_data_daily_df.columns[get_new_data_daily_df.columns.str.contains("Unnamed")], axis=1, inplace=True)
# get_new_data_daily_df


# combine datasets of old ultimatum and newly generated data
new_data_df = pd.concat([get_new_data_daily_df, data_df], ignore_index=True) # for ultimate_backup_file
# new_data_df

# st.write("NEW_DATA_DF")
# new_data_df = new_data_df.drop("Unnamed", axis=0)
# new_data_df.columns
# st.write(data_df["movie_rating"].dtype)

nan_rows = new_data_df[new_data_df.isna().any(axis=1)]
# st.write(f"rows with nan valuesn : {len(nan_rows)} ") # 53

## CLEAN DATAFRAME
clean_data_df = new_data_df.dropna()
# clean_data_df.to_csv("./moviescrapper/data/all_movie_data.csv") added data to ultime_backup_file
## GET NUMBER OF DUPLICATES
duplicated = clean_data_df.duplicated().value_counts()

clean_data_df = clean_data_df.drop_duplicates()



# check datatypes
# column_data_types = clean_data_df.dtypes
# column_data_types


## get maximum values
highest_rating = clean_data_df["movie_rating"].max()
lowest_rating = clean_data_df["movie_rating"].min()

st.text(f"""Movie Ratings \n \t Highest Rating: {highest_rating} \n \t Lowest Rating: {lowest_rating}""")

# check the number of  ratings for each rate using value_counts
# st.write(clean_data_df["movie_rating"].value_counts())

movie_categories = ["Action", "Drama", "Comedy", "Horror", "Adventure", "Crime", "Sci-Fi", "Documentary"]
if entered_option == "year":
    movie_data_year_sorted_df = clean_data_df.sort_values(by=["movie_release_year"], ascending=False).reset_index(drop=True)
    # displaying movies after being sorted
    # movie_data_year_sorted_df

    movie_years = ["2024", "2023", "2025", "2022", "2017", "2015", "2016", "2018", "2019", "2014", "2021", "2010", "2020", "2012", "2004", "2009", "2013", "2006", "2007", "1999", "2011", "1986", "2001", "1985", "2008", "1995", "1989", "1990", "1998", "1991", "1987", "2000", "1966", "1988", "1956", "1997", "1973", "1982", "1984", "1992", "2002", "1968", "1970", "2005", "1972", "1934", "1964", "1976", "1967", "1930", "1977", "1958", "1978", "1959", "1962", "1971", "1965", "1979", "1950", "1969", "1983", "1996", "1926", "1975", "1961", "1931", "1954", "1994", "1980", "1938", "1923", "1948", "1928", "1949", "2003", "1947", "1939", "1946", "1920", "1974", "1929", "1993", "1951", "1981", "1933", "1937",
"1936"]
    movie_years.sort(reverse=True)
    default_value = movie_years.index("2025")
    yes_no_options = ["yes", "no"]
    yes_no_options_default = yes_no_options.index("yes")
    year_based_answer = st.sidebar.selectbox(f"View movies based on the year", movie_years, index=default_value)
    rating_option_answer = st.sidebar.selectbox("Rate movies in descending order", yes_no_options, index=yes_no_options_default)
    # st.sidebar.text(f"year_based_answer : {year_based_answer} and type : {type(year_based_answer)}")
    year = int(year_based_answer)
    # st.sidebar.text(f"Year value: {year} : type {type(year)}")
    # st.sidebar.text(f"rating_option_answer : {rating_option_answer}")


    for value in movie_years:
        year_value = int(value)
        if year_value == year:
            year_selected_movies_df = movie_data_year_sorted_df[movie_data_year_sorted_df["movie_release_year"] == year_value].reset_index(drop=True)
            if rating_option_answer == "yes":
                year_selected_rating_sorted_df = year_selected_movies_df.sort_values(by=["movie_rating"], ascending=False).reset_index(drop=True)
                year_selected_rating_sorted_df
            else:
                year_selected_movies_df
else:
    category_entered = st.sidebar.selectbox("Select the category of the movie you wish to view:", movie_categories)
    movie_data_category_based_df = clean_data_df[clean_data_df["movie_category"] == category_entered].reset_index(drop=True)
    
    yes_no_options = ["yes", "no"]
    two_option_answer = st.sidebar.selectbox(f"Get movies with highest rating in {category_entered}", yes_no_options)

    if two_option_answer == "yes":
        movie_data_category_sorted_based_df = movie_data_category_based_df.sort_values(by=["movie_rating"], ascending=False).reset_index(drop=True)
        movie_data_category_sorted_based_df
    else:
        movie_data_category_based_df